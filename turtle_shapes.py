# Drawing shapes using turtle
# Some functions for future references

import turtle

def draw_sq(x, y, size = 50):
    turtle.penup()
    turtle.goto(x-(x/2), y+(y/2))
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

# draw_sq(50, 50, 100)
# turtle.done()

def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"({x},{y})")
    turtle.goto(turtle.xcor(), turtle.ycor() - radius)
    turtle.pendown()
    turtle.circle(radius)

# draw_circle(50, 100, 50)
# turtle.done()

def draw_rectangle(coor1, coor2):
    turtle.penup()
    turtle.goto(coor1)
    turtle.pendown()

    turtle.goto(coor2[0], coor1[1])
    turtle.goto(coor2)
    turtle.goto(coor1[0], coor2[1])
    turtle.goto(coor1)

# draw_rectangle((10, 10), (23, 34))
# turtle.done()
