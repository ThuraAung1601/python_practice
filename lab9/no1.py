from tkinter import *

window = Tk()
global n
n = 0

def add():
    global n
    n += 1
    num = Label(window, text=n)
    num.grid(row=0, column=0)

def subtract():
    global n 
    n -= 1
    num = Label(window, text=n)
    num.grid(row=0, column=0)

def reset():
    global n 
    n = 0
    num = Label(window, text=n)
    num.grid(row=0, column=0)

num = Label(window, text=n)
num.grid(row=0, column=0)

adder = Button(window, text="+", padx=20, command= lambda: add())
adder.grid(row=0, column=1)

substractor = Button(window, text="-", padx=20, command= lambda: subtract())
substractor.grid(row=1, column=1)

reseter = Button(window, text="Reset", padx=20, command= lambda: reset())
reseter.grid(row=2, column=1)

window.mainloop()