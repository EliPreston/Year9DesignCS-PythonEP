import tkinter as tk

def change(*args):
	print("running change")
	print(var.get())

root = tk.Tk() #Constructs our main window

#List of strings
#The list is called options there are 3 elements with index 0 to 2
#print(OPTIONS[2])
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


root.mainloop()
print("END Program")