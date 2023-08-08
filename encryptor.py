from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


class Cipher:
    def __init__(self, encryptedText, key, iv):
        self.encryptedText = encryptedText
        self.key = key
        self.iv = iv



class AESEncryptor:

    def encrypt(self, text):
        # Generating a security key 
        key = get_random_bytes(32)
        # Converting the string into a bytes object
        data = text.encode('latin-1')
        # Creating the cipher object and encrypt the data
        cipher_encrypt = AES.new(key, AES.MODE_CFB)
        ciphered_bytes = cipher_encrypt.encrypt(data)
        # Storing the encrypted data, key and iv as a Cipher object
        return Cipher(ciphered_bytes.decode('latin-1'), key, cipher_encrypt.iv)

    def decrypt(self, encryptedCipher):
        # Decrypting the data using the Cipher object
        cipher_decrypt = AES.new(encryptedCipher.key, AES.MODE_CFB, iv=encryptedCipher.iv)
        deciphered_bytes = cipher_decrypt.decrypt(encryptedCipher.encryptedText.encode('latin-1'))
        # Convert the bytes object back to the string
        decrypted_data = deciphered_bytes.decode('latin-1')
        # Returning the original text
        return decrypted_data