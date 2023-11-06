import turtle

def spiral_pattern(side_length, sides):
    if sides == 0:
        return
    else:
        turtle.forward(side_length)
        turtle.right(90)
        spiral_pattern(side_length + 5, sides - 1)

spiral_pattern(10, 100)
turtle.done()