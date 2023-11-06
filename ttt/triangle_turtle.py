import turtle

def sierpinski_triangle(side_length, depth):
    if depth == 0:
        for _ in range(3):
            turtle.forward(side_length)
            turtle.left(120)
    else:
        side_length /= 2.0
        sierpinski_triangle(side_length, depth-1)
        turtle.forward(side_length)
        sierpinski_triangle(side_length, depth-1)
        turtle.backward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.right(60)
        sierpinski_triangle(side_length, depth-1)
        turtle.left(60)
        turtle.backward(side_length)
        turtle.right(60)

sierpinski_triangle(300, 3)
turtle.done()