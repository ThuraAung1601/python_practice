import turtle

def maxi_mini(ls):
    maxi, mini = ls[0], ls[0]
    for i in ls:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return maxi, mini

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y-1)
        turtle.pendown()
        turtle.circle(1)

class Rectangle2D(object):
    def __init__(self, minx=0, miny=0, maxx=0, maxy=0):
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
    def getRectange(self, points):
        self.maxx, self.minx = maxi_mini([pt.x for pt in points])
        self.maxy, self.miny = maxi_mini([pt.y for pt in points])
        self.width = self.maxx - self.minx
        self.height = self.maxy - self.miny
        self.centerx, self.centery = (self.width/2)+self.minx, (self.height/2)+self.miny

        turtle.penup()
        turtle.goto(self.minx, self.maxy)
        turtle.pendown()
        for i in range(2):
            turtle.forward(self.width)
            turtle.right(90)
            turtle.forward(self.height)
            turtle.right(90)

        print(f"The bounding rectange is centered at ({self.centerx}, {self.centery}) with width {self.width} and height {self.height}")


pt_input = input("Enter the points: ")
pt_ls = pt_input.split(" ")
if len(pt_ls) % 2 != 0:
    print("Invalid input: Missing one coorinate.")

point_list = []
for i in range(len(pt_ls)):
    if i == 0 or i%2 == 0:
        x, y = eval(pt_ls[i]), eval(pt_ls[i+1])
        # print(Point(x, y))
        point_list.append(Point(x, y))
# print(maxi_mini([pt.x for pt in point_list]))

for p in point_list:
    p.draw()

rec = Rectangle2D()
rec.getRectange(point_list)

turtle.done()
    