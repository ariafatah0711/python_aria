from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
root.resizable(False, False)

def time():
    string = strftime("%H:%M:%S %p") # 24 hours
    # string = strftime("%I:%M:%S %p") # 12 hours
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()