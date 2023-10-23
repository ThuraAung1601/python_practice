'''
No.5
Write a program to display a recursive tree.
'''
import math
from tkinter import * 

def display():
    canvas.delete("line")
    displayRTree(int(order.get()), width/2, height-100, height / 3, math.pi / 2)

def displayRTree(depth, x1, y1, length, angle):
    if depth >= 0:
        x2 = x1 - math.cos(angle) * length
        y2 = y1 - math.sin(angle) * length
        # Draw the line
        canvas.create_line(x1, y1, x2, y2, tag="line")
        # Draw the left branch
        displayRTree(depth - 1, x2, y2, length * sizeFactor, angle + angleFactor)
        # Draw the right branch
        displayRTree(depth - 1, x2, y2, length * sizeFactor, angle - angleFactor)

window = Tk()
window.title("Recursive tree")

width = 600
height = 600
canvas = Canvas(window, width=width, height=height)
canvas.pack()

frame1 = Frame(window) 
frame1.pack()
angleFactor = math.pi / 5
sizeFactor = 0.6
Label(frame1, text="Enter an order: ").pack(side=LEFT)
order = StringVar()

entry = Entry(frame1, textvariable=order, justify=RIGHT).pack(side=LEFT)
Button(frame1, text="Display Recursive tree", command=display).pack(side=LEFT)

window.mainloop() 