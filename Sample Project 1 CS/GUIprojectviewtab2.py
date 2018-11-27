import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
















root = tk.Tk()
root.title("The Elements Study Tool")
root.geometry("600x600")
root.configure(background= 'grey')
root.resizable(False,False)



labA = tk.Label(root, text= "What Element would you like to find?")
labA.config(background= 'grey')
labA.grid(row = 0, column = 0, sticky = "w")

entE = tk.Entry(root, width = 20)
entE.config(background= 'grey')
entE.grid(row = 1, column = 0, sticky = "w")

outputEL = tk.Text(root, width = 20, height = 7, borderwidth=3, relief=tk.GROOVE)
outputEL.config(state = "disabled", background= 'grey')
outputEL.grid(row = 2, column = 0, sticky = "w")

btnEF = tk.Button(root, text= "Find Element")
btnEF.config(background= 'grey')
btnEF.grid(row = 1, column = 1, sticky = "w")




root.mainloop()