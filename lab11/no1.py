'''
Create a constructor for Point and Circle 
and print the informations
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printInformation(self):
        return "{} {}".format(self.x, self.y)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def printInformation(self):
        print(super().printInformation()) 
        print("From circle class:\n{} {}".format(self.x, self.y))
        print("radius is {} and area is {}".format(self.radius, 3.142*self.radius**2))

pt = Point(1,1)
pt.printInformation()

circle = Circle(1, 1, 10)
circle.printInformation()