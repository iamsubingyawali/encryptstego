import os.path


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
