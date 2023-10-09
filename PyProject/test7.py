from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200") 

frame = ttk.Frame(root, borderwidth=2, relief='solid')
frame.grid()

def change():
    str = int(spinbox.get())
    print(str-5)

spinbox = ttk.Spinbox(from_=1.0, to=100.0, command=change)
spinbox.grid(row=1, column=1)
 
root.mainloop()