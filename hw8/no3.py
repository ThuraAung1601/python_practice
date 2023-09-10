'''
No.3
Write a Python program for reading a string from the user then drawing a bar graph
for the count of each character occuring in the string using the turtle module.
Note: each bar has the height of 20 times of its character count,
and the height of the vertical axis will be the same as the height of
the tallest bar.
'''
import turtle
def freq_distri(text):
    freq = {}
    for c in text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def make_arrow_head():
    x,y = turtle.xcor(), turtle.ycor()
    turtle.left(135)
    turtle.forward(10)
    turtle.goto(x,y)
    turtle.right(135)
    turtle.right(135)
    turtle.forward(10)
    turtle.backward(10)
    turtle.left(135)

def draw_bar_graph(f):
    vertical = max(list(f.values()))
    turtle.left(90)
    turtle.forward(vertical*20)
    make_arrow_head()
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90)
    turtle.pendown()
    for i in range(len(f)):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.left(90)
        x,y = turtle.xcor(), turtle.ycor()
        turtle.penup()
        turtle.goto(x-5,y-10)
        turtle.write(list(f.keys())[i])
        turtle.goto(x,y)
        turtle.pendown()

    turtle.forward(20)
    make_arrow_head()
    turtle.goto(0,0)

def main():
    text = input("Enter some text:")
    f = freq_distri(text)
    draw_bar_graph(f)
    turtle.done()

main()
