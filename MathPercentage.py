import tkinter as tk
import os
#I would have the score out of lets say 15
#You would get a score of for example 13 out of 15

def submit():

	print("Submit pressed")
	x = float(entx.get())

	y = x/15*100
	
	output.config(state="normal")

	outputValue = "Score:"+str(y)+"%"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")

root = tk.Tk()
root.title("Volume of a Cylinder") 


labx = tk.Label(root, text="Score")
labx.configure(background="red")
labx.pack()

entx = tk.Entry(root)
entx.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()