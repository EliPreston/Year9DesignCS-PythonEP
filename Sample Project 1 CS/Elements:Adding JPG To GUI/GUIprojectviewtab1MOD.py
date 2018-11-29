import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image



elements = ["Hydrogen"]


def submitA(*args):	
	print("You have answered")
	print(entA.get())
	labA.config(foreground="white")
	outputRW.config(state="normal")

	value = entA.get()

	loc = -1

	for i in range (0, len(elements), 1):
		if elements[i] == value:
			loc = [i]

	if loc != -1:
		outputValue = ("Correct")	
		outputRW.delete(1.0,tk.END)
		outputRW.insert(tk.INSERT,outputValue)
		outputRW.config(state="disabled")

	else:
		outputValue = ("Wrong")
		outputRW.delete(1.0,tk.END)
		outputRW.insert(tk.INSERT,outputValue)
		outputRW.config(state="disabled")


description = ["This is used in rocket fuel", "This has to do with party balloons"]

def Hint(*args):
	print("Getting Hint")	
	outputH.config(state="normal")

	outputValue = (description[0])	

	outputH.delete(1.0,tk.END)
	outputH.insert(tk.INSERT,outputValue)
	outputH.config(state="disabled")

 








root = tk.Tk()
root.title("The Elements Study Tool")
root.geometry("600x600")
root.configure(background= 'grey' )
root.resizable(False,False)




labT = tk.Label(root, text= "The Periodic Table Quiz")
labT.config(background= 'grey')
labT.grid(row = 0, column = 0, columnspan = 2)

btnS = tk.Button(root, text="Start")
btnS.grid(row = 1, column = 0, sticky = "w")

labP = tk.Label(root, text= "Points During Quiz")
labP.config(background= 'grey')
labP.grid(row = 2, column = 0, columnspan = 2, sticky = "w")

outputP = tk.Text(root, width=10, height=1, borderwidth=3, relief=tk.GROOVE)
outputP.config(state="disabled", background= 'grey')
outputP.grid(row = 3, column = 0, sticky = "w")

labFP = tk.Label(root, text= "Final Score")
labFP.config(background= 'grey')
labFP.grid(row = 4, column = 0, columnspan = 2, sticky = "w")

outputFS = tk.Text(root, width=15, height=3, borderwidth=3, relief=tk.GROOVE)
outputFS.config(state="disabled", background= 'grey')
outputFS.grid(row = 5, column = 0, sticky = "w")


#********* COLUMN 2/3 ******************

labT = tk.Label(root, text= "This will be a timer")
labT.config(background= 'grey')
labT.grid(row = 1, column = 3, columnspan = 2, sticky = "w")

labO = tk.Label(root, text= "Other Information")
labO.config(background= 'grey')
labO.grid(row = 2, column = 3, columnspan = 3, sticky = "w")

outputP = tk.Text(root, width=10, height=1, borderwidth=3, relief=tk.GROOVE)
outputP.config(state="disabled", background= 'grey')
outputP.grid(row = 3, column = 0, sticky = "w")

btnH = tk.Button(root, text="Hint?", command=Hint)
btnH.config()
btnH.grid(row = 4, column = 3, sticky = "w")

outputH = tk.Text(root, width=15, height=3, borderwidth=3, relief=tk.GROOVE)
outputH.config(state="disabled", background= 'grey')
outputH.grid(row = 5, column = 3, sticky = "w")

#********* COLUMN 6 ******************

path = "1_Hydrogen.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img, width = 250, height = 100)
panel.grid(row = 1, column = 6)


labA = tk.Label(root, text= "Your Answer")
labA.config(background= 'grey')
labA.grid(row = 2, column = 6, sticky = "w")
labA.bind("<Button-1>",submitA)

entA = tk.Entry(root, width=15, borderwidth=3)
entA.config(background= 'grey')
entA.grid(row = 3, column = 6, sticky = "w")


labRA = tk.Label(root, text= "This will output a right or wrong text")
labRA.config(background= 'grey')
labRA.grid(row = 4, column = 6, sticky = "w")

outputRW = tk.Text(root, width = 15, height = 3, borderwidth=3, relief=tk.GROOVE)
outputRW.config(state = "disabled", background= 'grey')
outputRW.grid(row = 5, column = 6, sticky = "w")
















root.mainloop()







