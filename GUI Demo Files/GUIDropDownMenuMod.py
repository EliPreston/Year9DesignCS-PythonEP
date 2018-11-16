import tkinter as tk
import os
import math

def change(*args):
	print("running change")
	print(var.get())

root = tk.Tk()

OPTIONS = [
	"1",
	"2",
	"3",
]


var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()



lab = tk.Label(root, text="Help")
lab.configure(background="white")
lab.pack()

entr = tk.Entry()
entr.pack()

root.mainloop()
print("Program Terminated")