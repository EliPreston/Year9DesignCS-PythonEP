import tkinter as tk

root = tk.Tk()
root.title("GUI Canvas")
root.resizable(False,False)

#The root.resizable(False, False) and root.max/minsize do the same thing pretty much

#root.maxsize(1440,900)
#root.minsize(500,500)
canvas1 = tk.Canvas(root, width=720, height=720, background="black")

canvas1.pack();


canvas1.create_polygon(10, 10, 20, 30, 30, 20, fill="red")
canvas1.create_line(10, 10, 100, 100, fill="red")
canvas1.create_text(125, 100, text="Origin", fill="blue")

canvas1.create_line(20, 40, 20, 200, fill="red")
canvas1.create_polygon(15, 200, 25, 200, 20, 230, fill="red")
canvas1.create_text(60, 185, text="Positive y", fill="blue")

canvas1.create_line(40, 20, 220, 20, fill="red")
canvas1.create_polygon(200, 15, 200, 25, 230, 20, fill="red")
canvas1.create_text(170, 40, text="Positive x", fill="blue")

canvas1.create_rectangle(150, 400, 220, 480, fill="green")
canvas1.create_oval(146, 396, 154, 404, fill="purple")
canvas1.create_oval(216, 476, 224, 484, fill="purple")
canvas1.create_text(110, 400, text="(150,400)", fill="purple")
canvas1.create_text(260, 480, text="220, 480)", fill="purple")


root.mainloop()