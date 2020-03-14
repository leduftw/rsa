""" Algorithms related to discrete mathematics. """

import random
from math import sqrt, ceil


def fme(base: int, exponent: int, modulus: int) -> int:
    """ Algorithm for fast modular exponentiation. """
    result = 1
    temp = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * temp) % modulus
        temp = (temp * temp) % modulus
        exponent >>= 1
    return result


def gcd(a: int, b: int) -> int:
    """ Euclidean algorithm for calculating greatest common divisor. """
    while b != 0:
        (a, b) = (b, a % b)
    return a


def xgcd(a: int, b: int) -> tuple:
    """ Extended Euclidean algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a: int, modulus: int) -> int:
    """ Returns x such that (x * a) % modulus == 1. Relies on extended Euclidean algorithm. """
    g, x, _ = xgcd(a, modulus)
    if g != 1:
        raise Exception("gcd(a, modulus) != 1")
    return x % modulus


def is_prime(n: int) -> bool:
    """ Checks whether n is prime or not. """
    if n < 10 ** 12:  # for relatively small n run deterministic test (O(sqrt(n)))
        return is_prime_deterministic(n)
    else:  # otherwise run non-deterministic test
        return fermat(n)


def is_prime_deterministic(n: int) -> bool:
    if n < 2:
        return False
    elif n < 4:
        return True

    # All primes are of the form 6k +- 1
    if n % 6 != 1 and n % 6 != 5:
        return False

    for i in range(5, ceil(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fermat(n: int) -> bool:
    """ Fermat's primality test.  """
    if n < 2:
        return False
    if n < 4:
        return True

    # Increase for higher probability of determining
    # whether a number is actually prime.
    k = 50  # number of iterations
    for i in range(k):
        a = random.randrange(2, n - 1)  # 1 < a < n - 1
        if gcd(a, n) != 1:
            return False  # it's definitely not prime
        if fme(a, n - 1, n) != 1:
            return False  # it's definitely not prime
    return True  # it's probably prime


def factorize(n: int) -> tuple:
    """ Returns pair of primes (p, q) such that p*q = n. """
    """ 
    # This is much faster, but we first need to create file with prime numbers.
    # This can be done using Sieve of Erathostenes.
    
    # U primes.txt se nalazi prvih 53 326 267 prostih brojeva (prosti brojevi < 1 000 000 000)
    # Velicina fajla je 513MB. Fajl je generisan za nekih 10 sekundi uz pomoc Eratostenovog sita.
    with open("primes.txt") as primes:
        for line in primes:
            for prime in map(int, line.split()):
                if n % prime == 0:
                    return prime, n // prime
    return 1, 1
    """
    # For min(p, q) < 100 000 000 we can wait, but for larger p and q it will take a lot of time
    for divisor in range(2, int(sqrt(n)) + 1):
        if n % divisor == 0:
            return divisor, n // divisor
    return 1, 1  # this will never be executed
