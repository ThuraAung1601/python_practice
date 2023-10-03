import turtle
import no4

class Square(no4.TwoDshape):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    def draw(self):
        turtle.penup()
        # turtle.goto(self.x-(self.x/2), self.y+(self.y/2))
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)
        turtle.penup()
