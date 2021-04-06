import hashlib
import os.path
from Crypto.Cipher import AES


# class Decode to handle decoding activities
class Decode:
    # Parameterized constructor to receive image path and password while object initialization
    def __init__(self, image_path, password):
        self.image_path = image_path
        self.password = password.strip()

    # method to check if the supplied password is valid
    # returns true if the password is valid else returns false
    def is_password_valid(self):
        # checking if the password is empty
        if len(self.password) == 0:
            return False
        return True

    # method to check if the supplied path of the image is valid and image file exists
    # returns true if the path is valid else returns false
    def is_image_path_valid(self):
        # checking if the image exists on given path
        if os.path.exists(self.image_path):
            return True
        return False

    def get_decoded_text(self, binary_value):
        # generating a 32 bytes hex key from the provided password in order to use it as aes secret key
        secret_key = hashlib.sha1(str(self.password).encode()).hexdigest()[:32]
        # creating new PyCrypto AES object to decrypt the converted bytes
        decryption_key = AES.new(secret_key.encode('utf-8'), AES.MODE_EAX, secret_key.encode())
        # Source:
        # https://stackoverflow.com/questions/40343414/how-to-convert-binary-string-to-byte-like-object-in-python-3
        # converting extracted binary values into bytes
        bytes_value = bytes([int(binary_value[b:b + 8], 2) for b in range(0, len(binary_value), 8)])
        # decrypting and returning the extracted text
        return decryption_key.decrypt(bytes_value).decode('utf-8')

    # method to check for all the supplied values and pass the error messages accordingly
    # returns status and message for validity check
    def are_values_valid(self):
        # calling above methods one by one to check if password and image path are valid
        if not self.is_password_valid():
            return ["Password can't be empty.", False]
        elif not self.is_image_path_valid():
            return ["Selected image doesn't exist anymore.", False]
        else:
            return ["Valid", True]
