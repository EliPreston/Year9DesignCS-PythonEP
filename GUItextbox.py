import tkinter as tk


root = tk.Tk()
root.title("GUI Text Box")
text1 = tk.Text(root, height=10, width=50)
#Changing the entire content


text1.config(font="helvetica 30",background="blue", foreground="yellow")


text1.insert(tk.INSERT,"Line 1\n")
text1.insert(tk.INSERT,"Line 2")
text1.insert(1.5, "*")
text1.insert(2.5, "*")

text1.tag_add("tag1",1.0,1.4)
text1.tag_config("tag1",background="black", foreground="white")

text1.tag_add("tag2",2.0,2.4)
text1.tag_config("tag2",background="black", foreground="white")

text1.config(state="disabled")


text1.pack()

root.mainloop()