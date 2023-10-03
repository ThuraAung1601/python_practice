import turtle
from abc import ABC, abstractmethod

class TwoDshape(ABC):
    def __init__(self, x, y):
        self.x = x,
        self.y = y
        pass

    @abstractmethod
    def draw(self):
        pass        

class Line(TwoDshape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        turtle.pendown()
        turtle.goto(self.x, self.y)
        turtle.penup()

class Circle(TwoDshape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.write(f"({self.x},{self.y})")
        turtle.goto(turtle.xcor(), turtle.ycor() - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()

class Rectangle(TwoDshape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto(self.x + self.width, self.y)
        turtle.goto(self.x + self.width, self.y + self.height)
        turtle.goto(self.x, self.y + self.height)
        turtle.goto(self.x, self.y)
        turtle.penup()
