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
        turtle.penup()
        # Adjust starting position based on initial square size
        turtle.goto(turtle.xcor()+g, turtle.ycor()-g)  
        turtle.pendown() 
        # Reduce the size for the next inner square 
        s -= 2 * g  

# Function to draw nested squares with a gap
def draw_nested_spiral_squares(s, g):
    draw_square(s)
    s = s - (2 * g)
    while s >= 5:
        turtle.penup()
        # Adjust starting position based on initial square size
        turtle.goto(turtle.xcor()+g, turtle.ycor()-g) 
        # Rotate the square
        turtle.left(10) 
        turtle.pendown() 
        draw_square(s)
        # Reduce the size for the next inner square 
        s = s - (2 * g) 

# Size of the outermost square
initial_size = 150
# Gap between inner squares  
gap = 20

draw_nested_squares(initial_size, gap)  # Drawing the nested squares
# draw_nested_spiral_squares(initial_size, gap)
turtle.done()
