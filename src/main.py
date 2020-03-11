from src.rsa import *
from timeit import default_timer as timer


def main():
    # Najvece dozvoljeno slovo je V (ASCII 86) jer je 86 - 54 = 32
    # Ostala veca slova W, X, Y, Z ne mogu zbog mod 33
    # Ako je poruka napisana na srpskom jeziku, samo Z ce se izgubiti

    # Prvi zadatak
    n, e = 3233, 101
    pub_key = PublicKey(n, e)
    start = timer()
    private_key = PrivateKey.calculate_private_key(pub_key)
    end = timer()
    print(f"Private key is: {private_key}")
    print(f"Calculated in {end - start} seconds.\n")

    # Drugi zadatak
    n = 33
    e = [3, 9, 7]
    public_keys = []
    for _ in e:
        public_keys.append(PublicKey(n, _))
    first_crypto = [30, 11, 20, 7, 11, 32, 16, 23, 2, 6, 9, 20, 25, 6, 25]
    second_crypto = [16, 8, 14, 3, 8, 6, 4, 26, 3, 21, 4, 26, 4, 32, 11, 6, 4]
    third_crypto = [21, 19, 13, 5, 24, 31, 8, 19, 11, 25, 13, 26, 11]
    examples = [first_crypto, second_crypto, third_crypto]
    for test in zip(examples, public_keys):
        print(brute_force_decrypt_from_numbers(test[0], test[1]))
    print()

    # Testiranje
    """
    message = "Dusko Sretenovic"
    p, q = 999995621, 999995629
    # p = 2 ** 100 - 15
    # q = 2 ** 97 - 141
    n, e = p*q, 1433
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
    """
    # num_primes()


if __name__ == "__main__":
    main()
