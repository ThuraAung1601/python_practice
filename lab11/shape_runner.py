import no4
import no5
import turtle

shapes = []

r1 = no4.Rectangle(-50, -50, 30, 20)
# r1.draw()
shapes.append(r1)

l1 = no4.Line(40, 0)
# l1.draw()
shapes.append(l1)

c1 = no4.Circle(20, 20, 30)
# c1.draw()
shapes.append(c1)

s1 = no5.Square(30, 30, 80)
shapes.append(s1)

for s in shapes:
    s.draw()

turtle.done()