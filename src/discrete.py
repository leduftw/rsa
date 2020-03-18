""" Algorithms related to discrete mathematics. """


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
    """
    Extended Euclidean algorithm.
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
