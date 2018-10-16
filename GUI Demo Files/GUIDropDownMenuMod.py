import tkinter as tk
import os
import math

def change(*args):
	print("running change")
	print(var.get())

root = tk.Tk()

OPTIONS = [
	"eggs",
	"bunny",
	"chicken",
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()


labrO1 = tk.Label(OPTIONS, text="Radius")
labrO1.configure(background="blue")
labrO1.pack()

root.mainloop()
print("END Program")