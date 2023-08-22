import turtle
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lower_x = x + width 
        self.lower_y = y - height
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return (self.width*2) + (self.height*2)
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for i in range(0,2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.r = radius
    def getArea(self):
        return 3.142*self.r*self.r
    def getPerimeter(self):
        return 2*3.142*self.r
    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y + self.r)
        turtle.write(f"{self.x}, {self.y}")
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.circle(self.r)

# r1 = Rectangle(-50, 50, 160, 80)
# r1.draw()
# print(r1.getArea())
# r1.move(1,2)
# r1.draw()

turtle.speed(1)
c1 = Circle(-20, 50, 30)
c1.draw()
c1.move(1,2)
c1.draw()
turtle.done()