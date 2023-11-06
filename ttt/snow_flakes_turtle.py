import turtle

def koch_snowflake(side_length, depth):
    if depth == 0:
        turtle.forward(side_length)
    else:
        side_length /= 3.0
        koch_snowflake(side_length, depth-1)
        turtle.left(60)
        koch_snowflake(side_length, depth-1)
        turtle.right(120)
        koch_snowflake(side_length, depth-1)
        turtle.left(60)
        koch_snowflake(side_length, depth-1)

koch_snowflake(300, 4)
turtle.done()