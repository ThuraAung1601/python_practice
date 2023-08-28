import turtle

def draw_sq(size):
    turtle.penup()
    turtle.forward(size/2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size/2)

def draw_nested_squares(s,g):
    while s >= 20:
        draw_sq(s)
        turtle.write(s)
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        s -= 2 * g

draw_nested_squares(200, 20)
turtle.done()
