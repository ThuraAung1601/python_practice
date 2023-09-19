from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.grid(row=0, column=0)
canvas. create_rectangle(20, 20, 370, 220)

def addLine(event):
    r = lambda: random.randint(0, 255)
    color = "#%02X%02X%02X" % (r(), r(), r())
    if event.x not in range(20, 370) or event.y not in range(20, 370):
        new_window = Toplevel(window)
        new_window.title("Warning")

        text = "Mouse pointer is not in the rectangle."
        label = Label(new_window, text=text)
        label.pack()

        exit_button = Button(new_window, text="Ok", command=lambda: new_window.destroy)
        exit_button.pack()
    else:
        canvas.create_oval(event.x - 5, event.y + 5, event.x + 5, event.y -5, fill=color )

canvas.bind("<Button-1>", addLine)
window.mainloop()