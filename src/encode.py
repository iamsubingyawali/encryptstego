import os.path


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
        # the ord function converts each character of the given text to unicode value
        # the format function formats it into binary
        # the join function joins binary value of each character on loop
        binary_value = ''.join(format(ord(character), '08b') for character in self.text_to_encode)
        return len(binary_value)

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
