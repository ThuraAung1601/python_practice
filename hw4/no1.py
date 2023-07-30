'''
No.1
Write a program that prompts the user to enter the x- and y-coordinates for the
three points p0, p1, and p2 and the program then displays a message to indicate 
whether p2 is on the left side of the line, the right side, or on the line between p0 and p1.
'''

import turtle

print("Suppose P0 is always on the left of P1.")
x0,y0 = eval(input("Enter x0,y0 for point P0: "))
x1,y1 = eval(input("Enter x1,y1 for point P1: "))
x2,y2 = eval(input("Enter x2,y2 for point P2: "))

turtle.penup()
turtle.goto(x0,y0)
turtle.write("P0")
turtle.pendown()

turtle.goto(x1,y1)
turtle.write("P1")

turtle.penup()
turtle.goto(x2,y2)
turtle.write("P2")
turtle.pendown()

# Slope of the line from P0 to P1
m0 = (y1-y0)/(x1-x0)
# Slope of the line fron P0 to P2
m1 = (y2-y0)/(x2-x0)

if m0 > 0 and m1 > 0: 
    if m0 < m1: out = "P2 is on the left side of the line P0 to P1."
    elif m0 > m1: out = "P2 is on the right side of the line P0 to P1."
    else: out = "P2 is on the same line with P0 and P1."

#elif (m0 > 0 and m1 < 0) or (m0 < 0 and m1 > 0) or (m0 < 0 and m1 < 0):
else:
    if m0 > m1: out = "P2 is on the left side of the line P0 to P1."
    elif m0 < m1: out = "P2 is on the right side of the line P0 to P1."
    else: out = "P2 is on the line between P0 and P1."

turtle.penup()
turtle.sety(-50)
turtle.write(out)
turtle.pendown()
print(out)

turtle.done()