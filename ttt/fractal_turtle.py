import turtle
def fractal_tree(branch_length, depth):
    if depth == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        fractal_tree(branch_length/2, depth-1)
        turtle.right(90)
        fractal_tree(branch_length/2, depth-1)
        turtle.left(45)
        turtle.backward(branch_length)

turtle.left(90)
fractal_tree(200, 5)

turtle.done()