'''
Write a simple turtle interpreter with python.
'''
import turtle

while True:
    interact = input("turtle |> ")

    if interact == "fd":
        step = input("Please input its argument:")
        turtle.forward(eval(step))
    elif interact == "back":
        step = input("Please input its argument:")
        turtle.backward(eval(step))
    elif interact == "lt":
        step = input("Please input its argument:")
        turtle.left(eval(step))
    elif interact == "rt":
        step = input("Please input its argument:")
        turtle.right(eval(step))

    elif interact == "pu":
        turtle.penup()
    elif interact == "pd":
        turtle.pendown()
    
    elif interact == "reset":
        turtle.clear()
        turtle.reset()

    elif interact == "quit":
        break

    else:
        print("Wrong command, please try again.")   