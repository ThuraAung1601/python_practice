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

def star(length):
    inner_degree = 36
    outer_degree = 180 - 36
    turtle.showturtle()
    for i in range(5):
        turtle.forward(length)
        turtle.right(outer_degree)
        turtle.forward(length)

# star(30)
# turtle.done()

def triangle(coor1, coor2, coor3):
    x1, y1 = coor1[0], coor1[1]
    x2, y2 = coor2[0], coor2[1]
    x3, y3 = coor3[0], coor3[1]
    # Side 1
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.write((x1,y1))
    turtle.pendown()
    # Side 2
    turtle.goto(x2,y2)
    turtle.write((x2,y2))
    # Side 3
    turtle.goto(x3,y3)
    turtle.write((x3,y3))

    turtle.goto(x1,y1)
    turtle.pendown()

# triangle((1,1), (30, 12), (20, 20))
# turtle.done()
