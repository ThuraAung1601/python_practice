import turtle

def draw_sq(size):
    i = 1
    while i <= 4:
        turtle.forward(size)
        turtle.left(90)
        i += 1

for j in range(4):
    for i in range(5):
        draw_sq(50*i)
    turtle.right(90)

turtle.done()
