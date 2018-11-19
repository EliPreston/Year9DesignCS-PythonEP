import tkinter as tk


def onReturn(event):
	print("Return Pressed")

	value = entry1.get();
	print(value)


	entry1.delete(0, 'end')


root = tk. Tk()
root.title("GUI Entry With Return")


entry1 = tk.Entry(root)

entry1.bind("<Return>", onReturn)

entry1.pack()

root.mainloop()
