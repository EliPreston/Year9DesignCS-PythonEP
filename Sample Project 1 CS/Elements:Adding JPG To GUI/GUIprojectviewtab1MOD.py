import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import random


def start(*args):
	print("Starting Quiz")
	print("Other Information:")	
	outputOI.config(state="normal")
	outputP.config(state="normal")
	outputH.config(state="normal")


	randomelement = random.randint(0,3)

	data[0] = random.randint(0,len(fileName) - 1)

	outputValue = (otherinformation[data[0]])

	outputOI.delete(1.0,tk.END)
	outputOI.insert(tk.INSERT,outputValue)
	outputOI.config(state="disabled")


	outputValue1 = (points)

	outputP.delete(1.0,tk.END)
	outputP.insert(tk.INSERT,points)
	outputP.config(state="disabled")	

	outputH.delete(1.0,tk.END)
	outputH.config(state="disabled")

	print(data[0])
	#LOAD YOUR IMAGE BASED ON fileName[num]

	#img = ImageTk.PhotoImage(Image.open(fileName[num]))
	#panel.config(image = img)






def submitA(*args):	
	labA.config(foreground="purple", background="black")
	outputRW.config(state="normal")
	outputP.config(state="normal")
	print("You have answered")
	print(entA.get())
	
	#pointsDefault = 0

	value = entA.get()

	loc = -1

	for i in range (0, len(elements), 1):
		if elements[i] == value:
			loc = [i]

		if loc != -1:
			outputValue1 = ("Correct")
			outputRW.delete(1.0,tk.END)
			outputRW.insert(tk.INSERT,outputValue1)
			outputRW.config(state="disabled")
			
			"""
			outputP.delete(1.0,tk.END)
			outputP.insert(tk.INSERT,pointsDefault+1)
			outputRW.config(state="disabled")
			"""

		else:
			outputValue = ("Wrong")
			outputRW.delete(1.0,tk.END)
			outputRW.insert(tk.INSERT,outputValue)
			outputRW.config(state="disabled")


def Hint(*args):
	print("Getting Hint")	
	outputH.config(state="normal")

	print("*****************"+str(data[0])+"*****************")
	outputValue = (description[data[0]])
	

	outputH.delete(1.0,tk.END)
	outputH.insert(tk.INSERT,outputValue)
	outputH.config(state="disabled")
	



#*******************************************

root = tk.Tk()
root.title("Elements Study Tool")
root.configure(background="#90AFC5")
root.resizable(False, False)

#*******************************************

points = 0

#data is list that stores state data,  data[0] is my randomized num
data = [0]

fileName = ["1_Hydrogen.jpg","2_Helium.jpg","3_Lithium.jpg"]

otherinformation = ["Used in rockets", "Used in party balloons", "Lithium other information"]

elements = ["Hydrogen", "Helium", "Lithium"]

description = ["This is used in rocket fuel", "This has to do with party balloons", "Lithium hint"]




#****************** COLUMN 1 #******************
labT = tk.Label(root, text = "Periodic Quiz", background = "#0366D6", foreground = "white", height = 2)
labT.config()
labT.grid(row = 0, column = 0, columnspan = 2, sticky= "w")

btnS = tk.Button(root, text="Quiz Me!")
btnS.grid(row = 1, column = 0, sticky = "w")
btnS.bind("<Button-1>",start)

labP = tk.Label(root, text= "Points")
labP.config(background= '#90AFC5')
labP.grid(row = 2, column = 0, columnspan = 2, sticky = "w")

outputP = tk.Text(root, width=10, height=1, borderwidth=3, relief=tk.GROOVE)
outputP.config(state="disabled", background= 'grey')
outputP.grid(row = 3, column = 0, sticky = "w")






#****************** COLUMN 2/3 #******************
#labT = tk.Label(root, text= "This will be a timer")
#labT.config(background= 'grey')
#labT.grid(row = 1, column = 3, columnspan = 2, sticky = "w")

labOI = tk.Label(root, text= "Other Information")
labOI.config(background= '#90AFC5')
labOI.grid(row = 2, column = 3, columnspan = 3, sticky = "w")
#labOI.bind("<Button-1>",start)

outputOI = tk.Text(root, width=15, height=3, borderwidth=3, relief=tk.GROOVE)
outputOI.config(state="disabled", background= 'grey')
outputOI.grid(row = 3, column = 3, sticky = "w")

labH = tk.Button(root, text="Hint?")
#labH.config()
labH.grid(row = 4, column = 3, sticky = "w")
labH.bind("<Button-1>",Hint)

outputH = tk.Text(root, width=15, height=3, borderwidth=3, relief=tk.GROOVE)
outputH.config(state="disabled", background= 'grey')
outputH.grid(row = 5, column = 3, sticky = "w")






#****************** COLUMN 6 #******************
num = random.randint(0,len(fileName) - 1)
img = ImageTk.PhotoImage(Image.open(fileName[num]))

panel = tk.Label(root)
panel.grid(row = 1, column = 6)


labA = tk.Button(root, text= "Your Answer", command = submitA)
#labA.config(fg= '#DB4437')
labA.grid(row = 2, column = 6, sticky = "w")
#labA.bind("<Button-1>",submitA)

entA = tk.Entry(root, width=15, borderwidth=3)
entA.config(background= 'grey')
entA.grid(row = 3, column = 6, sticky = "w")

outputRW = tk.Text(root, width = 15, height = 3, borderwidth=3, relief=tk.GROOVE)
outputRW.config(state = "disabled", background= 'grey')
outputRW.grid(row = 5, column = 6, sticky = "w")





root.mainloop()










