""" Some functionalities that have no use right now. """

from src.rsa import *
from timeit import default_timer as timer


def brute_force_decrypt_number(crypto: int, public_key: PublicKey) -> int:
    """ Decrypts given number with public key (n, e). """
    private_key = PrivateKey.calculate_private_key(public_key)
    return fme(crypto, private_key.d, private_key.n)


def encrypt(message: str, public_key: PublicKey) -> str:
    """ Interface for encrypting messages with public key. """
    msg = message.replace(" ", "").upper()  # remove spaces and convert to uppercase
    number_message = to_numbers(msg)
    for i, number in enumerate(number_message):
        number_message[i] = encrypt_number(number, public_key)
    return to_letters(number_message)


def decrypt(crypto: str, private_key: PrivateKey) -> str:
    """ Interface for decrypting messages with private key. """
    number_crypto = to_numbers(crypto)
    for i, number in enumerate(number_crypto):
        number_crypto[i] = decrypt_number(number, private_key)
    return to_letters(number_crypto)


def brute_force_decrypt(crypto: str, public_key: PublicKey) -> str:
    """ Interface for brute force decryption of given message. """
    number_crypto = to_numbers(crypto)
    private_key = PrivateKey.calculate_private_key(public_key)
    for i, number in enumerate(number_crypto):
        number_crypto[i] = decrypt_number(number, private_key)
    return to_letters(number_crypto)


def main():
    # Testiranje
    message = "Dvwusko Sretenovicz"
    p, q = 3, 11
    # p = 2 ** 100 - 15
    # q = 2 ** 97 - 141
    n, e = p*q, 7
    public_key = PublicKey(n, e)
    print(public_key)

    crypto = encrypt_to_numbers(message, public_key)
    print(f"Original message: {message}")
    print(f"Encrypted: {crypto}")

    start = timer()
    private_key = PrivateKey.calculate_private_key(public_key)
    end = timer()
    print(private_key)
    decrypted = decrypt_from_numbers(crypto, private_key)
    print(f"Decrypted: {decrypted}")
    print(f"Message decrypted in {end - start} seconds.")


if __name__ == "__main__":
    main()
