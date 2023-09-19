from tkinter import *

window = Tk()
window.title("Currency Converter")

e = Entry(window, width=50)
e.grid(row=0, column=0)

def to_thb():
    usd = abs(float(e.get()))
    thb = usd * 30
    new_window = Toplevel(window)
    new_window.title("USD -> THB")
    text = f"{usd:.2f} USD = {thb:.2f} THB"
    label = Label(new_window, text=text)
    label.pack()
    exit_button = Button(new_window, text="OK", command=new_window.destroy)
    exit_button.pack()

def to_usd():
    thb = abs(float(e.get()))
    usd = thb / 30
    new_window = Toplevel(window)
    new_window.title("THB -> USD")
    text = f"{thb:.2f} THB = {usd:.2f} USD"
    label = Label(new_window, text=text)
    label.pack()
    exit_button = Button(new_window, text="OK", command=new_window.destroy)
    exit_button.pack()

thb_button = Button(window, text="USD -> THB", command = lambda: to_thb())
thb_button.grid(row=1, column=0)
usd_button = Button(window, text="THB -> USD", command = lambda: to_usd())
usd_button.grid(row=2, column=0)

window.mainloop()