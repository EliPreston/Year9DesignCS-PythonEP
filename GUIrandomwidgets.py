import tkinter as tk



root = tk.Tk()
root.title("Example") 

canvas1 = tk.Canvas(root, width=100, height=100, background="black")
canvas1.pack();

lab = tk.Label(root, text="input")
lab.configure(background="red")
lab.pack()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width=20, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()