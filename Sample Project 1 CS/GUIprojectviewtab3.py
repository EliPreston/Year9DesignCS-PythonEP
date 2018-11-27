import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image



def clicked1(event):
	#How do i decide who i have clicked on
	print('high to low')
	labAR.config(background= "black", foreground = 'white')
	labAR2.config(background = 'grey', foreground = 'white')


def clicked2(event):
	#How do i decide who i have clicked on
	print('low to high')
	labAR.config(background= "grey", foreground = 'white')
	labAR2.config(background = 'black', foreground = 'white')

	














root = tk.Tk()
root.title("The Elements Study Tool")
root.geometry("600x600")
root.configure(background= 'grey')
root.resizable(False,False)





#btnAR = tk.Button(root, text= "High to Low") #command=submit)
#btnAR.config(background= 'grey')
#btnAR.grid(row = 0, column = 0)
labAR = tk.Label(root, text= 'high to low')
labAR.config(background= "grey")
labAR.grid(row = 0, column = 0)
labAR.bind('<button-1>', clicked1)




outputAR = tk.Text(root, width = 20, height = 7, borderwidth=3, relief=tk.GROOVE)
outputAR.config(state = "disabled", background= 'grey')
outputAR.grid(row = 1, column = 0, sticky = "w")



#btnAR2 = tk.Button(root, text= "Low to High")
#btnAR2.config(background= 'grey')
#btnAR2.grid(row = 0, column = 1)
labAR2 = tk.Label(root, text= 'high to low')
labAR2.config(background= "grey")
labAR2.grid(row = 1, column = 0)
labAR2.bind('<button-1>', clicked2 )






outputAR2 = tk.Text(root, width = 20, height = 7, borderwidth=3, relief=tk.GROOVE)
outputAR2.config(state = "disabled", background= 'grey')
outputAR2.grid(row = 1, column = 1, sticky = "w")



root.mainloop()

