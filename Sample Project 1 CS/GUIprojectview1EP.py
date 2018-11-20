import tkinter as tk
from tkinter import ttk
from tkinter import *


root = tk.Tk()
root.title("The Elements Study Tool")
root.geometry("600x600")
root.configure(background= 'grey' )
root.resizable(False,False)


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="QUIZ WINDOW")
tabControl.pack(expand=1, fill="both");



#********* COLUMN 1 ******************

labTt1 = tk.Label(tab1, text= "The Periodic Table Quiz")
labTt1.config()
labTt1.grid(row = 0, column = 0, columnspan = 2)

btnSt1 = tk.Button(tab1, text="Start")
btnSt1.grid(row = 4, column = 0, sticky = "w")

labPt1 = tk.Label(tab1, text= "Points During Quiz")
labPt1.config()
labPt1.grid(row = 6, column = 0, columnspan = 2, sticky = "w")

outputPt1 = tk.Text(tab1, width=10, height=1, borderwidth=3, relief=tk.GROOVE)
outputPt1.config(state="disabled")
outputPt1.grid(row = 7, column = 0, sticky = "w")

labFPt1 = tk.Label(tab1, text= "Final Score")
labFPt1.config()
labFPt1.grid(row = 8, column = 0, columnspan = 2, sticky = "w")

outputFSt1 = tk.Text(tab1, width=10, height=1, borderwidth=3, relief=tk.GROOVE)
outputFSt1.config(state="disabled")
outputFSt1.grid(row = 9, column = 0, sticky = "w")


#********* COLUMN 2/3 ******************

labTt1 = tk.Label(tab1, text= "This will be a timer")
labTt1.config()
labTt1.grid(row = 2, column = 3, columnspan = 2, sticky = "w")

labOt1 = tk.Label(tab1, text= "Other Information")
labOt1.config()
labOt1.grid(row = 4, column = 3, columnspan = 3, sticky = "w")

outputOt1 = tk.Text(tab1, width=16, height=6, borderwidth=3, relief=tk.GROOVE)
outputOt1.config(state="disabled")
outputOt1.grid(row = 5, column = 3, sticky = "w")

btnHt1 = tk.Button(tab1, text="Hint?")
btnHt1.grid(row = 6, column = 3, sticky = "w")

outputHt1 = tk.Text(tab1, width=16, height=3, borderwidth=3, relief=tk.GROOVE)
outputHt1.config(state="disabled")
outputHt1.grid(row = 7, column = 3, sticky = "w")

#********* COLUMN 6 ******************

labIt1 = tk.Label(tab1, text= "This should be an image")
labIt1.config()
labIt1.grid(row = 3, column = 6, sticky = "w")

labAt1 = tk.Label(tab1, text= "Your Answer")
labAt1.config()
labAt1.grid(row = 6, column = 6, sticky = "w")

entA = tk.Entry(tab1)
entA.grid(row = 7, column = 6, sticky = "w")




labRAt1 = tk.Label(tab1, text= "Right? or Wrong?")
labRAt1.config()
labRAt1.grid(row = 8, column = 6, sticky = "w")

outputRWt1 = tk.Text(tab1, width = 10, height = 1, borderwidth=3, relief=tk.GROOVE)
outputRWt1.config(state = "disabled")
outputRWt1.grid(row = 9, column = 6, sticky = "w")

#*******************************************************************************

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="The Elements")
tabControl.pack(expand=1, fill="both");


labAt2 = tk.Label(tab2, text= "What Element would you like to find?")
labAt2.config()
labAt2.grid(row = 0, column = 0, sticky = "w")

entE = tk.Entry(tab2)
entE.grid(row = 1, column = 0, sticky = "w")

outputELt2 = tk.Text(tab2, width = 20, height = 7, borderwidth=3, relief=tk.GROOVE)
outputELt2.config(state = "disabled")
outputELt2.grid(row = 2, column = 0, sticky = "w")


#*******************************************************************************




tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Previous Scores")
tabControl.pack(expand=1, fill="both");





root.mainloop()








