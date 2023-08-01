'''
No.2
Write a program that prompts the user to enter the
center x-, y-coordinates, width, and height of two rectangles and determines
whether the second rectangle is inside the first or overlaps with the first.
'''
import turtle

x1,y1 = eval(input("Enter x1,y1 for center of rectangle 1: "))
w1,h1 = eval(input("Enter width and height w1,h1 for rectangle 1: "))

x2,y2 = eval(input("Enter x2,y2 for center of rectangle 2: "))
w2,h2 = eval(input("Enter width and height w2,h2 for rectangle 2: "))

xDistance = abs(x1 - x2)
yDistance = abs(y1 - y2)

if w1 > w2 and h1 > h2:
    if xDistance <= (w1 - w2) / 2 and yDistance <= (h1 - h2) / 2:
        print("Rectangle 2 is inside Rectangle 1")
    elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
        print("Rectangle 2  overlaps Rectangle 1")
    else:
        print("Rectangle 2 does not overlap Rectangle 1")
else:
    if xDistance <= (w2 - w1) / 2 and yDistance <= (h2 - h1) / 2:
        print("Rectangle 1 is inside Rectangle 2")
    elif xDistance <= (w1 + w2) / 2 and yDistance <= (h1 + h2) / 2:
        print("Rectangle 1 overlaps Rectangle 2")
    else:
        print("Rectangle 1 does not overlap Rectangle 2")

def draw(x,y,w,h):
    '''
    Draw rectangles using coordinates x,y and width w and height h
    '''
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(w/2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(h/2)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h/2)
    turtle.left(90)

# to validate with visual content
draw(x1,y1,w1,h1)
draw(x2,y2,w2,h2)

turtle.done()
