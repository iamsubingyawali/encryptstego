# Importing required libraries
import tkinter as tk
from ctypes import windll
import Crypto

window = tk.Tk()
window.title("Encryptstego")
window.geometry('800x500')
window.resizable(False, False)
windll.shcore.SetProcessDpiAwareness(1)

photo = tk.PhotoImage(file="../images/logo.png")
window.iconphoto(True, photo)

window.mainloop()
