import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo, askyesno

win = tk.Tk()
win.withdraw()
password = askstring('Password', 'Enter password:\t\t\t\t', show="*")
showinfo('Show password', f'password input: {password}')


# ---------------------------------------

from tkinter import filedialog

win = tk.Tk()
win.withdraw()

file_path = filedialog.askopenfilename()

showinfo('Pfadname', f'Pfadname aus FileDialog: {file_path}')