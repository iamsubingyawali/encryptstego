<h1 align="center">Encryptstego</h1>
<p align="center">
  <img height="150" width="150" src="images/logo.png"/>
</p>
<p align="center">Python GUI based application for Image Steganography, with encryption and Key based LSB substitution</p></br>

### `Installation`

Before installing this application on any OS environment, clone this repo using the command below in your terminal or command prompt or powershell prompt.

```sh
git clone https://github.com/iamsubingyawali/encryptstego.git
```

### `Installation on Windows`

It is pretty simple to install and run this application on Windows. There are two ways one can can run this app on Windows.

1. Using installer

   Navigate to the cloned folder and inside the "Setup" folder, a windows application installer is available. Run the installer, follow the on-screen instructions and done. You can launch the app      from the start menu.

2. Manual installation
   
   The manual installation on Windows is same as the installation on Linux and Mac environments. See Linux/Mac installation section to manually install the app.
   
   
### `Installation on Linux/Mac`

First clone the repo using the command above and navigate to the cloned directory. Then run the command below to install all the dependencies. If the system has multiple versions of Python and pip installed, use version 3.

```sh
cd encryptstego
pip install -r requirements.txt
```

After all the dependencies are installed, just run the main file using the command below. The program GUI should open.

```sh
python encryptstego.py
```

### `Usage`

This application can be used to embed the text messages into images. The main window has two options Encode and Decode. As the names suggest, the Encode button is used to encode the text into images while the Decode button is used to decode the texts from encoded images.

For encoding, a password must be provided. The password is used to encrypt the text before encoding as well as to dynamically select the pixels to embed the data into.

For decoding, the correct image with encoded text must be used. The password must be correct. Without the correct passwoes, the text can never be extracted from the image.

</br><p><b>Open an issue if any errors occur while using the app. You can also contribute to the project for further enhancements.</b><p></br>

<p align="center">Made with ❤ and Python</p>

