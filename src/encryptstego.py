# Importing required libraries
from tkinter import *
# windll is Windows OS specific, so must be commented before running on other environments
from ctypes import windll
from PIL import ImageTk, Image


def open_encode_window():
    encode_window = Toplevel(window)
    # Setting title of the encode window
    encode_window.title("Encryptstego - Encode")
    # Setting the size of the encode window
    encode_window.geometry('800x500')
    # Setting the resizable property of the encode window to false
    encode_window.resizable(False, False)
    # Setting the encode window to be DPI aware for different screens
    # windll is Windows OS specific, so must be commented before running on other environments
    windll.shcore.SetProcessDpiAwareness(1)
    # Test label
    new_label = Label(encode_window, text="This is encode window")
    new_label.pack()


def open_decode_window():
    decode_window = Toplevel(window)
    # Setting title of the decode window
    decode_window.title("Encryptstego - Encode")
    # Setting the size of the decode window
    decode_window.geometry('800x500')
    # Setting the resizable property of the decode window to false
    decode_window.resizable(False, False)
    # Setting the decode window to be DPI aware for different screens
    # windll is Windows OS specific, so must be commented before running on other environments
    windll.shcore.SetProcessDpiAwareness(1)
    # Test label
    new_label = Label(decode_window, text="This is decode window")
    new_label.pack()


# Initializing tkinter window
window = Tk()
# Setting title of the window
window.title("Encryptstego")
# Setting the size of the window
window.geometry('800x500')
# Setting the resizable property of the window to false
window.resizable(False, False)
# Setting the window to be DPI aware for different screens
# windll is Windows OS specific, so must be commented before running on other environments
windll.shcore.SetProcessDpiAwareness(1)

# Getting the logo image for displaying on window as well as title
logo = Image.open("../images/logo.png")
# Resizing the image for proper view
logo = logo.resize((100, 100), Image.ANTIALIAS)
# Creating PhotoImage object from the image
logo = ImageTk.PhotoImage(logo)
# Setting the title icon of the window
window.iconphoto(True, logo)

# Initializing label to display image on the window
image_label = Label(window, image=logo, height=100, width=100)
# Packing the label on the window
image_label.pack(pady=20)

# Initializing label to display title label on the window
title_label = Label(window, text="Encryptstego")
# Packing the label on the window
title_label.pack()
# Setting font configurations for the label - font family and font size
title_label.config(font=("Open Sans", 32))

# Initializing button for encode action
encode_btn = Button(window, text="Encode", height=2, width=15, bg="#503066", fg="white", borderwidth=0,
                    command=open_encode_window)
# Setting font configurations for the button - font family, font size and font weight
encode_btn.config(font=("Open Sans", 15, "bold"))
# Packing the button on the window
encode_btn.pack(side=LEFT, padx=50)

# Initializing button for the decode button
decode_btn = Button(window, text="Decode", height=2, width=15, bg="#36923B", fg="white", borderwidth=0,
                    command=open_decode_window)
# Setting font configurations for the button - font family, font size and font weight
decode_btn.config(font=("Open Sans", 15, "bold"))
# Packing the button on the window
decode_btn.pack(side=RIGHT, padx=50)

# Initializing footer name label
footer_label = Label(window, text="Subin Gyawali")
# Packing the label on the window
footer_label.pack(side=BOTTOM, pady=20)

# Terminating the execution with mainloop
window.mainloop()
