import turtle
def cross(width, times):
  if times == 0:
    turtle.dot(3, "black")
    return 
  else:
    for i in range(4):
      turtle.forward(width)
      cross(width/2, times-1)
      turtle.right(180)
      turtle.forward(width)
      turtle.left(90)

cross(100, 4)
turtle.done()