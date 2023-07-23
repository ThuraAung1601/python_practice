import turtle
import math

x1,y1 = eval(input("Enter x1 and y1 for point 1: "))
x2,y2 = eval(input("Enter x2 and y2 for point 2: "))
x3,y3 = eval(input("Enter x3 and y3 for point 3: "))

# Triangle drawing
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

# Euclidean distance
side1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
side2 = math.sqrt((x3-x2)**2+(y3-y2)**2)
side3 = math.sqrt((x1-x3)**2+(y1-y3)**2)

# Ref: Y. Daniel liang, Chapter 2, Ex 2.14, Page 58, Introduction to Programming using Python. 
s = (side1 + side2 + side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

message = "The area of the triangle is {}".format(area)

turtle.penup()
# Move the turtle 100 units below the origin
turtle.sety(-100)  
turtle.write(message)
turtle.pendown()
turtle.done()
