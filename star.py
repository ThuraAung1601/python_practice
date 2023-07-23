import turtle

length = int(input("Enter a length of the star:"))
inner_degree = 36
outer_degree = 180 - 36


turtle.showturtle()

turtle.forward(length)
turtle.right(outer_degree)
turtle.forward(length)

turtle.forward(length)
turtle.right(outer_degree)
turtle.forward(length)

turtle.forward(length)
turtle.right(outer_degree)
turtle.forward(length)

turtle.forward(length)
turtle.right(outer_degree)
turtle.forward(length)

turtle.forward(length)
turtle.right(outer_degree)
turtle.forward(length)

turtle.done()
