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

	outputValue = "Given\nRadius: "+str(r)+" units\nHeight: "+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	outputt1.delete(1.0,tk.END)
	outputt1.insert(tk.INSERT,outputValue)
	outputt1.config(state="disabled")


window = tk.Tk()
window.title("Calculators")
window.geometry("600x500")
window.configure(background='purple')

tabControl = ttk.Notebook(window)                                #Created tabcontrol

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
outputt1.config(font="helvetica 15", background="black", foreground="white")
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

	outputValue = "Given\nRadius: "+str(r)+" units\nHeight: "+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

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
outputt2.config(font="helvetica 15", background="black", foreground="white")
outputt2.config(state="disabled")
outputt2.pack()


#######################################################


tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Rectangular Prism Volume Calculator")
tabControl.pack(expand=1, fill="both")


def submit():

	print("Submit pressed")
	l = float(entlt3.get())
	w = float(entwt3.get())
	h = float(entht3.get())

	v = l*w*h
	v = round(v,3)

	outputt3.config(state="normal")

	outputValue = "Given\nLength: "+str(l)+" units\nWidth: "+str(w)+" units\nHeight: "+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	outputt3.delete(1.0,tk.END)
	outputt3.insert(tk.INSERT,outputValue)
	outputt3.config(state="disabled")



lablt3 = tk.Label(tab3, text="Length")
lablt3.configure(background="pink")
lablt3.pack()

entlt3 = tk.Entry(tab3)
entlt3.pack()

labwt3 = tk.Label(tab3, text="Width")
labwt3.configure(background="violet")
labwt3.pack()

entwt3 = tk.Entry(tab3)
entwt3.pack()

labht3 = tk.Label(tab3, text="Height")
labht3.configure(background="grey")
labht3.pack()

entht3 = tk.Entry(tab3)
entht3.pack()

btnt3 = tk.Button(tab3, text="Submit Numbers", command=submit)
btnt3.pack()

outputt3 = tk.Text(tab3, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
outputt3.config(font="helvetica 15", background="black", foreground="white")
outputt3.config(state="disabled")
outputt3.pack()




window.mainloop()



