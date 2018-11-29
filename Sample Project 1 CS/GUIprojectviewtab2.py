import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image



element_list = ["Hydrogen","Helium","Lithium","Berilym", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon"]
element_id = ["H","He","Li","Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe" ]


def find(*args):
	print("Finding Element...")
	print(entE.get())
	outputEL.config(state="normal")

	value = entE.get()
	#Step 1: Search the list for the location of the entry value
	loc = -1 #negative 1 means the value is NOT in the list element_id

	for i in range(0, len(element_list), 1):
		if element_list[i] == value:
			loc = i


	if loc != -1:
		outputValue = (element_id[loc])	
		outputEL.delete(1.0,tk.END)
		outputEL.insert(tk.INSERT,outputValue)
		outputEL.config(state="disabled")	

	else:
		outputValue = ("Element Not Found")
		outputEL.delete(1.0,tk.END)
		outputEL.insert(tk.INSERT,outputValue)
		outputEL.config(state="disabled")












root = tk.Tk()
root.title("List of the Elements")
root.geometry("600x600")
root.configure(background= 'grey')
root.resizable(False,False)



labA = tk.Label(root, text= "What Element would you like to find?")
labA.config(background= 'grey')
labA.grid(row = 0, column = 0, sticky = "w")

entE = tk.Entry(root, width = 20)
entE.config(background= 'grey')
entE.grid(row = 1, column = 0, sticky = "w")

btnEF = tk.Button(root, text= "Find Element", command=find)
btnEF.config(background= 'grey')
btnEF.grid(row = 2, column = 0, sticky = "w")
btnEF.bind("<Button-1>",find)

outputEL = tk.Text(root, width = 20, height = 7, borderwidth=3, relief=tk.GROOVE)
outputEL.config(state = "disabled", background= 'grey')
outputEL.grid(row = 3, column = 0, sticky = "w")





root.mainloop()




