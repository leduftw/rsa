""" Key handling. """

from src.prime import *


class Key:
    pass


class PublicKey(Key):
    def __init__(self, n: int, e: int) -> None:
        self.n = n
        self.e = e

    def __str__(self) -> str:
        return f"(n: {self.n}, e: {self.e})"


class PrivateKey(Key):
    def __init__(self, n: int, d: int) -> None:
        self.n = n
        self.d = d

    @classmethod
    def calculate_private_key(cls, public_key: PublicKey):
        p, q = factorize(public_key.n)  # n = p*q

        # phi(p*q) = phi(p)*phi(q) only works if gcd(p, q) == 1.
        # Since p and q are prime numbers, we only need to check for equality.
        if p != q:
            phi_n = (p - 1) * (q - 1)  # phi(n) = phi(p*q) = phi(p)*phi(q) = (p-1)*(q-1)
        else:
            raise Exception("p and q should not be equal!")
        d = modinv(public_key.e, phi_n)
        return cls(public_key.n, d)

    def __str__(self):
        return f"(n: {self.n}, d: {self.d})"
