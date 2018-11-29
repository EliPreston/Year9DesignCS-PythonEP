import tkinter as tk
from tkinter import *


root = tk.Tk()



path = "1_Hydrogen.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img, width = 250, height = 100)
panel.grid(row = 1, column = 6)




root.mainloop()
