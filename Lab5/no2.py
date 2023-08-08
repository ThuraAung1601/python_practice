import turtle

side = 100
N = 5
small_side = side/N
turtle.speed(0)
k = 1
while k <= N:
    j = 1
    while j <= N:
        i = 0
        while i <= 4:
            turtle.forward(small_side)
            turtle.left(90)
            i += 1 
        turtle.right(90)
        j += 1
    turtle.penup()
    turtle.goto(0,turtle.ycor()-small_side)
    turtle.pendown()
    k += 1
    
turtle.done()
