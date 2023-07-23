import turtle

# Turtle windows
turtle.Screen()
turtle.title("Home Sweet Home")
turtle.bgcolor("light blue")
turtle.pensize(2)

# circle as the sun
turtle.penup() 
# go to the top corner
turtle.goto(200,200) 
turtle.pendown()

# color of the sun as Yellow
turtle.fillcolor("Yellow")
# fill assigned color 
turtle.begin_fill()
# turtle will draw circle with radius 50 pixels  
turtle.circle(50) 
# stop filling assign color
turtle.end_fill() 

# parallelogram as the grass
turtle.penup()
turtle.goto(-400,-300) 
turtle.pendown()

# color of the grass is Green
turtle.fillcolor("Green") 
turtle.begin_fill()
# parellelogram is with 45 degree angle
# height = 200 and width = 700
turtle.forward(700) 
turtle.left(45)
turtle.forward(200)
turtle.left(135)
turtle.forward(700)
turtle.left(45)
turtle.forward(200)
turtle.end_fill()

# rectangle as the house
turtle.penup()
turtle.goto(300,0) 
turtle.pendown()

turtle.fillcolor("White")
turtle.begin_fill()
# rotate the turtle direction 
turtle.right(45) 
# height = 200 and width = 400
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# roof as a triangle 60 degree
turtle.fillcolor("Blue")
turtle.begin_fill()
turtle.left(60)
turtle.forward(230)
turtle.left(60)
turtle.forward(230)
turtle.end_fill()

# rotate the turtle direction
turtle.left(60)

# Door as a rectangle
# height and width = 100
turtle.fillcolor("White")
turtle.begin_fill()

turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

# Window as a rectangle
# height = 50 and width = 100
turtle.penup()
turtle.goto(250,-50)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

# Window design
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(100)

turtle.done() 
