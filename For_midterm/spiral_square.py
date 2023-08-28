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

def draw_spiral(n):
    degree = 10
    draw_sq(n)

    while n > 5:
        # go back to center
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()

        # update n size
        n = n * 0.75

        # rotate for spiral
        turtle.left(degree)
        draw_sq(n)

draw_spiral(150)
