import turtle

def draw_polygon(x,y,side=4,size=100):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    i = 0
    while i < side:
        turtle.forward(size)
        turtle.right(360/side)
        i += 1

draw_polygon(10,10,5,200)

turtle.done()