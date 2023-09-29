'''
No.1
Write a Python function to draw a Pie chart according to the number of occurences of
each integer in the list.
'''
import turtle
import random

# turtle.speed(1)
ls = [3,1,3,3,2,3,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]

def freq_distro(ls):
    freq = {}
    for i in ls:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq

def pie_chart(ls):
    turtle.Turtle()
    radius = 320
    prev_h = 0
    total_no = len(ls)
    freq = freq_distro(ls)
    prop = {}
    for i in ls:
        prop[i] = freq[i] / total_no
    # print(prop)
    for i in prop:
        turtle.pendown()
        # get the current heading for the pen
        current_h = 360 * prop[i]
        # print(ch)
        # random hexadeicmal number for color
        hexa_num = "#" + ''.join([random.choice("0123456789ABCDEF") for i in range(6)])
        # print(hexa_num)
        # print(f"Current header {current_h}, Previous header {prev_h}")

        turtle.fillcolor(hexa_num)
        turtle.begin_fill()
        turtle.forward(radius)
        turtle.left(90)
        turtle.circle(radius, current_h)
        turtle.penup()
        turtle.setpos(0,0)
        turtle.setheading(prev_h+current_h)
        turtle.end_fill()
        prev_h = prev_h + current_h
    
    turtle.done()

pie_chart(ls)
