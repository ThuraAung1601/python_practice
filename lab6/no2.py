import turtle
turtle.speed(3)

def draw_rectangle(size):
    i = 0
    while i < 4:
        turtle.forward(size)
        turtle.right(90)
        i += 1

def draw_nested_rectangle(size):
    for j in range(4):
        for i in range(4):
            draw_rectangle(size*(i+1))
        turtle.right(90)
    

draw_nested_rectangle(40)
turtle.done()