import tkinter as tk
import math

def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is: "+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")


root = tk.Tk() #Constructs main window
root.title("Volume of a Cylinder") #Configures the window

#Construct the element
labr = tk.Label(root, text="Radius")
#Configuer element/widget/object
labr.configure(background="blue")
#Pack the element put it on the window
labr.pack()

entr = tk.Entry(root)
entr.pack()

slide1 = tk.Scale(root, from_=0, to=100, resolution=0.25, orient=tk.HORIZONTAL)
slide1.pack()

labh = tk.Label(root, text="Height")
labh.configure(background="purple")
labh.pack()

enth = tk.Entry(root)
enth.pack()

slide2 = tk.Scale(root, from_=0, to=100, resolution=0.25, orient=tk.HORIZONTAL)
slide2.pack()

btn = tk.Button(root, text="Submit Numbers", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()





root.mainloop() #Displays the window, and sets up an "event d"
