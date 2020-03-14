from src.rsa import *
from timeit import default_timer as timer


def main():
    # PRVI ZADATAK
    n, e = 3233, 101
    pub_key = PublicKey(n, e)
    start = timer()
    private_key = PrivateKey.calculate_private_key(pub_key)
    end = timer()
    print(f"Private key is: {private_key}")
    print(f"Calculated in {end - start} seconds.\n")

    # DRUGI ZADATAK
    # Najvece dozvoljeno slovo je V (ASCII 86) jer je 86 - 54 = 32.
    # Ostala veca slova W, X, Y, Z ne mogu zbog mod 33.
    # Ako je poruka napisana na latinici na srpskom jeziku, samo Z ce se izgubiti.
    n = [33, 33, 33]
    e = [3, 9, 7]
    public_keys = [PublicKey(nn, ee) for nn, ee in zip(n, e)]

    first_crypto = [30, 11, 20, 7, 11, 32, 16, 23, 2, 6, 9, 20, 25, 6, 25]
    second_crypto = [16, 8, 14, 3, 8, 6, 4, 26, 3, 21, 4, 26, 4, 32, 11, 6, 4]
    third_crypto = [21, 19, 13, 5, 24, 31, 8, 19, 11, 25, 13, 26, 11]
    messages = [first_crypto, second_crypto, third_crypto]

    for message, public_key in zip(messages, public_keys):
        print(brute_force_decrypt_from_numbers(message, public_key))


if __name__ == "__main__":
    main()
