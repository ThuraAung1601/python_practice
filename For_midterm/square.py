import turtle

# Function to draw a square of size n
def draw_square(n):
    for _ in range(4):
        turtle.forward(n)
        turtle.right(90)

# Function to draw nested squares with a gap
def draw_nested_squares(s, g):
    while s >= 20:
        draw_square(s)
        turtle.write(s)
        turtle.penup()
        # Adjust starting position based on initial square size
        turtle.goto(turtle.xcor()+g, turtle.ycor()-g)  
        turtle.pendown() 
        # Reduce the size for the next inner square 
        s -= 2 * g      
# Size of the outermost square
initial_size = 150
# Gap between inner squares  
gap = 20

draw_nested_squares(initial_size, gap)  # Drawing the nested squares
turtle.done()
