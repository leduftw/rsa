""" Algorithms related to prime numbers.
Check out this website: https://www.alpertron.com.ar/ECM.HTM
"""

from math import ceil, sqrt
from src.discrete import *
import random


def is_prime(n: int) -> bool:
    """ Checks whether n is prime or not. """
    if n < 10 ** 12:  # for relatively small n run deterministic test (O(sqrt(n)))
        return is_prime_deterministic(n)
    else:  # otherwise run non-deterministic test
        # return fermat(n)
        return miller_rabin(n)


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
    """ Fermat's primality test. The probability that one iteration
    will return probably prime if n is composite is <= 1/2.
    Therefore if we try k different values of a the probability that
    all of them will pass for composite number n is less than 1 / 2**k.
    Current k is 50, which means P(error) = 2**-50 which is approximately 10**-15.
    """
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


def miller_rabin(n: int) -> bool:
    """ Miller-Rabin primality test. The probability that one iteration
    will return probably prime if n is composite is less than 1/4.
    Therefore if we try t different values of a the probability that
    all of them will pass for composite number n is less than 1 / 2**(2*t).
    Current t is 50, which means P(error) = 2**-100 which is approximately 10**-30.

    This is much better than Fermat's, thus Miller-Rabin primality test
    is prefered over Fermat's primality test.
    """
    if n < 2:
        return False
    if n < 4:
        return True

    if n & 1 == 0:  # if n is even and not 2 then it's not prime
        return False

    # n is now definitely odd so n - 1 has form 2**k * q.

    # Find q and k
    q, k = n - 1, 0
    while q & 1 == 0:
        k += 1
        q >>= 1

    class Break(Exception):
        pass

    t = 50  # number of iterations
    for _ in range(t):
        try:
            a = random.randrange(2, n - 1)  # 1 < a < n - 1
            if fme(a, q, n) == 1:
                raise Break  # it's probably prime, but try another iteration to increase probability
            for j in range(k):
                if fme(a, 2 ** j * q, n) == n - 1:
                    raise Break  # it's probably prime, but try another iteration to increase probability
            return False  # it's definitely composite
        except Break:
            pass
    return True


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


if __name__ == "__main__":
    n = [359334085968622831041960188598043661065388726959079837,
         359334085968622831041960188598043661065388726959079839,
         359334085968622831041960188598043661065388726959079841]
    for number in n:
        print(f'{number} - {miller_rabin(number)}')
