import tkinter as tk
from tkinter import ttk
import math
import os

def clicked():
	print("Button Clicked")

def hitReturn(event):
	print("Please Press The Submit Button")

def submit():

	print("Your Answer Has Been Calulated")
	r = float(entrt1.get())
	h = float(entht1.get())

	v = math.pi*r*r*h
	v = round(v,3)

	outputt1.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	outputt1.delete(1.0,tk.END)
	outputt1.insert(tk.INSERT,outputValue)
	outputt1.config(state="disabled")


root = tk.Tk()                                                 #Create instance
root.title("Calculators")                                      #Sets title

tabControl = ttk.Notebook(root)                                #Created tabcontrol

tab1 = ttk.Frame(tabControl)                                   #Create tab and put it in tab control
tabControl.add(tab1, text="Cylinder Volume Calculator")        #Add the tab
tabControl.pack(expand=1, fill="both");

labrt1 = tk.Label(tab1, text="Radius")
labrt1.configure(background="blue")
labrt1.pack()

entrt1 = tk.Entry(tab1)
entrt1.pack()
entrt1.bind("<Return>", hitReturn)


labht1 = tk.Label(tab1, text="Height")
labht1.configure(background="purple")
labht1.pack()

entht1 = tk.Entry(tab1)
entht1.pack()
entht1.bind("<Return>", hitReturn)


btnt1 = tk.Button(tab1, text="Submit Numbers", command=submit)
btnt1.pack()

outputt1 = tk.Text(tab1, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
outputt1.config(state="disabled")
outputt1.pack()






tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Cone Volume Calculator")
tabControl.pack(expand=1, fill="both")

def submit():

	print("Submit pressed")
	r = float(entrt2.get())
	h = float(entht2.get())

	v = math.pi*r*r*h/3
	v = round(v,3)

	outputt2.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	outputt2.delete(1.0,tk.END)
	outputt2.insert(tk.INSERT,outputValue)
	outputt2.config(state="disabled")




labrt2 = tk.Label(tab2, text="Radius")
labrt2.configure(background="yellow")
labrt2.pack()

entrt2 = tk.Entry(tab2)
entrt2.pack()

labht2 = tk.Label(tab2, text="Height")
labht2.configure(background="green")
labht2.pack()

entht2 = tk.Entry(tab2)
entht2.pack()

btnt2 = tk.Button(tab2, text="Submit Numbers", command=submit)
btnt2.pack()

outputt2 = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
outputt2.config(state="disabled")
outputt2.pack()



root.mainloop()



