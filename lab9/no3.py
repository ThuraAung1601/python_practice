from tkinter import *

window = Tk()
window.title("A Simple paint program.")

last_x, last_y = 0, 0
def xy(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def addLine(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y))
    last_x, last_y = event.x, event.y

canvas = Canvas(window, width=500, height=500)
canvas.grid(row=0, column=0, sticky=(N,W,E,S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.create_text(text="Drag the mouse to draw")

clear = Button(window, text="Clear", command=lambda: canvas.delete("all"))
clear.grid(row=1, column=0)
window.mainloop()