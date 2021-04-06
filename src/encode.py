import hashlib
import os.path
import sys

from Crypto.Cipher import AES


# class Encode to handle encoding activities
class Encode:
    # Parameterized constructor to receive image path,
    # password and text to be encoded while object initialization
    def __init__(self, image_path, password, text_to_encode):
        self.image_path = image_path
        self.password = password.strip()
        self.text_to_encode = text_to_encode.strip()

    # method to check if the supplied password is valid
    # returns true if the password is valid else returns false
    def is_password_valid(self):
        # checking if the password is empty
        if len(self.password) == 0:
            return False
        return True

    # method to check if the supplied text to be encoded is valid
    # returns true if the text is valid else returns false
    def is_text_valid(self):
        # checking if the given text to encode is empty
        if len(self.text_to_encode) == 0:
            return False
        return True

    # method to check if the supplied path of the image is valid and image exists
    # returns true if the path is valid else returns false
    def is_image_path_valid(self):
        # checking if the image exists on given path
        if os.path.exists(self.image_path):
            return True
        return False

    # method to get binary value of the supplied text to be encoded
    # returns the binary equivalent of the given text
    def get_text_binary(self):
        # generating a 32 bytes hex key from the provided password in order to use it as aes secret key
        secret_key = hashlib.sha1(str(self.password).encode()).hexdigest()[:32]
        # creating an PyCrypto AES object for encryption
        encryption_key = AES.new(secret_key.encode('utf-8'), AES.MODE_EAX, secret_key.encode())
        # generating encrypted text using the AES object and the text to be encoded
        # returns encrypted bytes
        encrypted_text = encryption_key.encrypt(self.text_to_encode.encode('utf-8'))
        # Source:
        # https://stackoverflow.com/questions/40343414/how-to-convert-binary-string-to-byte-like-object-in-python-3
        # generating binary value from the encrypted bytes
        # the format function formats encrypted bytes it into binary bits
        # the join function joins binary value of each character on loop
        binary_value = ''.join('{:08b}'.format(character) for character in bytes(encrypted_text))
        return binary_value

    # method to check for all the supplied values and pass the error messages accordingly
    # returns status and message for validity check
    def are_values_valid(self):
        # calling above methods one by one to check if password, image path and given text are valid
        if not self.is_password_valid():
            return ["Password can't be empty.", False]
        elif not self.is_text_valid():
            return ["Text to encode can't be empty.", False]
        elif not self.is_image_path_valid():
            return ["Selected image doesn't exist anymore.", False]
        else:
            return [self.get_text_binary(), True]
