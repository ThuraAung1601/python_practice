import turtle

def draw_0(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.pendown()    
    turtle.circle(50)

def draw_1(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x, y+50)
    turtle.pendown()
    turtle.left(45)
    turtle.forward(20)
    turtle.right(45+90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)

def draw_2(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x-25, y+15)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(-25, 180)
    turtle.right(45)
    turtle.forward(60)
    turtle.left(45+90)
    turtle.forward(50)

def draw_3(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x, y+25)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(-25, 270)
    turtle.right(180)
    turtle.circle(-25, 270)

def draw_4(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(25)

def draw_5(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x+25, y+75)
    turtle.pendown()
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.circle(-50, 180)

def draw_6(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x, y+25)
    turtle.pendown()
    turtle.circle(-25, -270)
    turtle.right(90)
    turtle.forward(50)

def draw_7(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.goto(x-25, y+45)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(30+90)
    turtle.forward(100)

def draw_8(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.pendown()
    turtle.circle(-25)
    turtle.circle(25)

def draw_9(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(f"{x}, {y}")
    turtle.pendown()
    turtle.circle(25)
    turtle.circle(25, 90)
    turtle.backward(50)

x, y = 100, 100
draw_9(x, y)
turtle.done()
