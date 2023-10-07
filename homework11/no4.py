import turtle
from abc import ABC, abstractmethod

class Char(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def draw(x, y):
        pass
    
    @abstractmethod
    def getWidth():
        pass

class Char0(Char):
    def __init__(self):
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.pendown()    
        turtle.circle(25)
        turtle.setheading(0)
    def getWidth():
        return 50

class Char1(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
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
        turtle.setheading(0)
    def getWidth():
        return 50

class Char2(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
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
        turtle.setheading(0)
    def getWidth():
        return 50

class Char3(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.goto(x, y+25)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(-25, 270)
        turtle.right(180)
        turtle.circle(-25, 270)
        turtle.setheading(0)
    def getWidth():
        return 100

class Char4(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
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
        turtle.setheading(0)
    def getWidth():
        return 50

class Char5(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
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
        turtle.setheading(0)
    def getWidth():
        return 50

class Char6(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.goto(x, y+25)
        turtle.pendown()
        turtle.circle(-25, -270)
        turtle.right(90)
        turtle.forward(50)
        turtle.setheading(0)
    def getWidth():
        return 50

class Char7(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.goto(x-25, y+45)
        turtle.pendown()
        turtle.forward(50)
        turtle.right(30+90)
        turtle.forward(100)
        turtle.setheading(0)
    def getWidth():
        return 50

class Char8(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.pendown()
        turtle.circle(-25)
        turtle.circle(25)
        turtle.setheading(0)
    def getWidth():
        return 50

class Char9(Char):
    def __init__(self) -> None:
        super().__init__()
    def draw(x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(f"{x}, {y}")
        turtle.pendown()
        turtle.circle(25)
        turtle.circle(25, 90)
        turtle.backward(50)
        turtle.setheading(0)
    def getWidth():
        return 50

def drawNum(x):
    xpos = -200
    num_dict = {
        '0': Char0,
        '1': Char1,
        '2': Char2,
        '3': Char3,
        '4': Char4,
        '5': Char5,
        '6': Char6,
        '7': Char7,
        '8': Char8,
        '9': Char9
    }
    for i in x:
        num_dict[i].draw(xpos, 0)
        xpos += num_dict[i].getWidth()

num = "0123456789"
drawNum(num)

turtle.done()