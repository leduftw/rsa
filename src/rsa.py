""" Functions for encryption and decryption of messages with RSA algorithm. """

from src.keys import *
from src.discrete import *


def encrypt_to_numbers(message: str, public_key: PublicKey) -> list:
    """ Interface for encrypting messages with public key. """
    msg = message.replace(" ", "").upper()  # remove spaces and convert to uppercase
    number_message = to_numbers(msg)
    for i, number in enumerate(number_message):
        number_message[i] = encrypt_number(number, public_key)
    return number_message


def decrypt_from_numbers(crypto: list, private_key: PrivateKey) -> str:
    """ Interface for decrypting messages with private key. """
    number_crypto = crypto.copy()
    for i, number in enumerate(number_crypto):
        number_crypto[i] = decrypt_number(number, private_key)
    return to_letters(number_crypto)


def brute_force_decrypt_from_numbers(crypto: list, public_key: PublicKey) -> str:
    """ Interface for brute force decryption of given message. """
    private_key = PrivateKey.calculate_private_key(public_key)
    return decrypt_from_numbers(crypto, private_key)


def encrypt_number(message: int, public_key: PublicKey) -> int:
    """ Encrypts given number with public key (n, e). """
    return fme(message, public_key.e, public_key.n)


def decrypt_number(crypto: int, private_key: PrivateKey) -> int:
    """ Decrypts given number with private key (n, d). """
    return fme(crypto, private_key.d, private_key.n)


def to_numbers(message: str) -> list:
    """ Turns every letter in the message into number as specified in the statement.
     Given message must be in uppercase and should not contain whitespaces.
     """
    result = []
    for char in message:
        result.append(ord(char) - 54)
    return result


def to_letters(number_message: list) -> str:
    """ Converts list of numbers into uppercase string.
    Numbers in list should be in range [11, 36] for proper ASCII decoding.
    [11, 36] + 54 = [65, 90], i.e. A-Z
    """
    result = number_message.copy()
    for i, number in enumerate(number_message):
        result[i] = chr(number + 54)
    return "".join(result)
