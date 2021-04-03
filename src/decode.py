class Decode:
    def __init__(self, image_path, password):
        self.image_path = image_path
        self.password = password

    def test(self):
        print(f"Image Path: {self.image_path} Password: {self.password}")
