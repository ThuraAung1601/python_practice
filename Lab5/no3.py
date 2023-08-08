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
        if (j+k)%2 == 0:
            turtle.fillcolor("black")
            turtle.begin_fill()
            while i <= 4:
                turtle.forward(small_side)
                turtle.left(90)
                i += 1
            turtle.end_fill()
        else:
            while i <= 4:
                turtle.forward(small_side)
                turtle.left(90)
                i += 1 
        turtle.right(90)
        print(j)
        j += 1

    turtle.penup()
    turtle.goto(0,turtle.ycor()-small_side)
    turtle.pendown()
    k += 1
    
turtle.done()