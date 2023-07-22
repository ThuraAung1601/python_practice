import turtle

radius = eval(input("Enter the radius:"))

# gap should change with radius
gap = radius / 4

turtle.pensize(5)
turtle.color("blue")
turtle.circle(radius)

turtle.penup()
# move forward to gap
turtle.forward(2*radius + gap)
turtle.pendown()

turtle.color("black")
turtle.circle(radius)

turtle.penup()
# because gap should be equally spread to 3 circles
turtle.backward(gap/3)
turtle.pendown()

turtle.left(90)
turtle.color("yellow")
turtle.circle(radius)

turtle.right(90)

turtle.penup()
turtle.forward(2*radius + gap)
turtle.pendown()

turtle.color("red")
turtle.circle(radius)

turtle.left(90)
turtle.color("green")
turtle.circle(radius)

turtle.done()