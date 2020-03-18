"""
Sieve algorithms. Sieve of Erathostenes and sieve of Atkin are implemented.
Website: http://compoasso.free.fr/primelistweb/page/prime/accueil_en.php
"""

import math


class Sieve:
    def __init__(self, n=1000) -> None:
        """ Creates Sieve object with initial upper limit for finding primes. """
        self.n = n

    def sieve(self, file: str) -> None:
        """ Generates all primes up to n and writes result in file with given name. """
        pass

    @staticmethod
    def write_to_file(flags: list, file: str, erathosten=True) -> None:
        with open(file, "w") as primes:
            if not erathosten:
                cnt = 1
                for number, flag in enumerate(flags):
                    if flag:
                        primes.write(str(number))
                        primes.write(" ")
                        cnt += 1
                        if cnt % 40 == 0:
                            primes.write("\n")
            else:
                cnt = 1
                for index, flag in enumerate(flags):
                    if flag:
                        if index == 0:
                            number = 2
                        else:
                            number = 2*index + 1
                        primes.write(str(number))
                        primes.write(" ")
                        cnt += 1
                        if cnt % 40 == 0:
                            primes.write("\n")


class ErathostenSieve(Sieve):
    def sieve(self, file: str) -> None:
        sqrt_limit = math.floor(math.sqrt(self.n)) + 1
        memory = self.n // 2
        primes = [True] * memory  # False -> composite, True -> prime

        for i in range(3, sqrt_limit, 2):
            if primes[i // 2]:
                for j in range((i * i) // 2, memory, i):
                    primes[j] = False

        Sieve.write_to_file(primes, file)


class AtkinSieve(Sieve):
    def sieve(self, file: str) -> None:
        """
        Sieve of Atkin uses binary quadratic forms.
        It should be faster then Sieve of Erathostenes but in this implementation that is not the case.
        Paper: https://www.ams.org/journals/mcom/2004-73-246/S0025-5718-03-01501-1/S0025-5718-03-01501-1.pdf
        """
        primes = [False] * self.n  # False -> composite, True -> prime
        self.first_round(primes)

        primes[2] = True
        primes[3] = True
        self.second_round(primes)

        Sieve.write_to_file(primes, file, erathosten=False)

    def first_round(self, primes: list) -> None:
        sqrt_limit = math.floor(math.sqrt(self.n)) + 1
        for x in range(1, sqrt_limit):
            for y in range(1, sqrt_limit):
                k = 4*x*x + y*y
                if k < self.n and (k % 12 == 1 or k % 12 == 5):
                    primes[k] = not primes[k]
                k = 3*x*x + y*y
                if k < self.n and k % 12 == 7:
                    primes[k] = not primes[k]
                if x > y:
                    k = 3*x*x - y*y
                    if k < self.n and k % 12 == 11:
                        primes[k] = not primes[k]

    def second_round(self, primes):
        sqrt_limit = math.floor(math.sqrt(self.n)) + 1
        for i in range(5, sqrt_limit + 1):
            if primes[i]:
                j = i * i
                for k in range(j, self.n, j):
                    primes[k] = False


if __name__ == '__main__':
    sieve = ErathostenSieve(100000000)
    sieve.sieve("primes_100_million_erathosten.txt")
