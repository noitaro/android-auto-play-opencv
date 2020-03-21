from tkinter import messagebox
from ctypes import *

class Winlib():

    title = "Resemara"
    
    def MessageBox(self, _message):
        user32 = windll.user32
        result = user32.MessageBoxW(0, _message, self.title, 0x00000040)
        print(result)