class Encode:
    def __init__(self, image_path, password, text_to_encode):
        self.image_path = image_path
        self.password = password
        self.text_to_encode = text_to_encode

    def test(self):
        print(f"Image Path: {self.image_path} Password: {self.password} Text: {self.text_to_encode}")
