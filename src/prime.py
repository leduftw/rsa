"""
Algorithms related to prime numbers.
Check out this website: https://www.alpertron.com.ar/ECM.HTM
"""

from src.discrete import *
from src.sieve import *
import math
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

    for i in range(5, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fermat(n: int) -> bool:
    """
    Fermat's primality test. The probability that one iteration
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
    """
    Miller-Rabin primality test. The probability that one iteration
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
    if n < 10**12:
        return factorize_small(n)
    else:
        return factorize_large(n)


def factorize_small(n: int) -> tuple:
    # For min(p, q) < 50 000 000 we can wait, but for larger p and q it will take a lot of time
    for divisor in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return divisor, n // divisor


def factorize_large(n: int) -> tuple:
    # This is much faster for larger numbers, but we first need to create file with prime numbers.
    # This can be done using Sieve of Erathostenes.
    if n > 10**18:
        return factorize_small(n)  # preventing large output files
    else:
        up_to = math.ceil(math.sqrt(n))
        sieve = ErathostenSieve(up_to)
        sieve.sieve(f"primes_{up_to}.txt")

        with open(f"primes_{up_to}.txt") as primes:
            for prime in [map(int, line.split()) for line in primes]:
                if n % prime == 0:
                    return prime, n // prime
        number = prime + 2
        while n % number != 0:
            number += 2
        return number, n // number


if __name__ == "__main__":
    n = [359334085968622831041960188598043661065388726959079837,
         359334085968622831041960188598043661065388726959079839,
         359334085968622831041960188598043661065388726959079841]
    for number in n:
        print(f'{number} - {miller_rabin(number)}')
