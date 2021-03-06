# Python GUI program for Image Steganography with encryption - Encryptstego v1.0
# Created by Subin Gyawali

# Importing required libraries
from tkinter import *
# windll is Windows OS specific, so must be commented before running on other environments
from ctypes import windll
from tkinter import filedialog

from PIL import ImageTk, Image

# Defining global variables to track if two child windows for encoding and decoding are in opened or closed state
encode_opened = False
decode_opened = False


##########################################################
# ENCODE WINDOW COMPONENTS
##########################################################
# function to open a new window for encoding functionality
def open_encode_window():
    # referencing global variable to reflect modification globally
    global encode_opened
    # checking if the window is already open
    if not encode_opened:
        # Initializing new child window for encoding functions
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
        # setting the value of global tracking variable to true
        encode_opened = True
        # assigning a handler to define the actions when the window is tried to close
        encode_window.protocol("WM_DELETE_WINDOW", lambda: close_encode_window(encode_window))


##########################################################
# DECODE WINDOW COMPONENTS
##########################################################
# function to open a new window for decoding functionality
def open_decode_window():
    # referencing global variable to reflect modification globally
    global decode_opened
    # checking if the window is already open
    if not decode_opened:
        # Initializing new child window for decoding functions
        decode_window = Toplevel(window)
        # Setting title of the decode window
        decode_window.title("Encryptstego - Decode")
        # Setting the size of the decode window
        decode_window.geometry('800x500')
        # Setting the resizable property of the decode window to false
        decode_window.resizable(False, False)
        # Setting the decode window to be DPI aware for different screens
        # windll is Windows OS specific, so must be commented before running on other environments
        windll.shcore.SetProcessDpiAwareness(1)

        # Label to display image after the image is selected from the file window
        stego_image_label = Label(decode_window, text="Select Stego Image", height=20, width=50, relief="solid", bg="#FFFFFF")
        # Placing the label on the window statically
        stego_image_label.place(x=20, y=20)

        text_to_decode_label = Label(decode_window, text="Decoded Text")
        text_to_decode_label.config(font=("Open Sans", 12))
        text_to_decode_label.place(x=400, y=20)

        text_to_decode = Text(decode_window, height=7, width=34)
        text_to_decode.config(relief="solid", font=("Open Sans", 15), state=DISABLED)
        text_to_decode.place(x=400, y=51)

        pass_to_decode_label = Label(decode_window, text="Password")
        pass_to_decode_label.config(font=("Open Sans", 12))
        pass_to_decode_label.place(x=400, y=262)

        pass_to_decode = Entry(decode_window, width=34)
        pass_to_decode.config(relief="solid", font=("Open Sans", 15), show="*")
        pass_to_decode.place(x=400, y=293)

        browse_stego_btn = Button(decode_window, text="Browse Stego Image", width=29)
        browse_stego_btn.config(font=("Open Sans", 15), bg="#503066", fg="white", borderwidth=0)
        browse_stego_btn.place(x=20, y=350)

        decode_stego_btn = Button(decode_window, text="Decode", width=15)
        decode_stego_btn.config(font=("Open Sans", 15), bg="#36923B", fg="white", borderwidth=0)
        decode_stego_btn.place(x=592, y=420)

        decode_opened = True
        # assigning a handler to define the actions when the window is tried to close
        decode_window.protocol("WM_DELETE_WINDOW", lambda: close_decode_window(decode_window))


##########################################################
# MAIN WINDOW COMPONENTS
##########################################################
# Function to define actions to be performed when encoding window is tried to closed
def close_encode_window(encode_window):
    # referencing global variable to reflect modification globally
    global encode_opened
    # Destroying the passed child encoding window
    encode_window.destroy()
    # Setting the value of global tracking variable to false to denote that window is closed
    encode_opened = False


# Function to define actions to be performed when decoding window is tried to closed
def close_decode_window(decode_window):
    # referencing global variable to reflect modification globally
    global decode_opened
    # Destroying the passed child encoding window
    decode_window.destroy()
    # Setting the value of global tracking variable to false to denote that window is closed
    decode_opened = False


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
