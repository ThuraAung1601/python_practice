import turtle
def freq_distri(ls):
    freq = {}
    for c in ls:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def make_arrow_head():
    x,y = turtle.xcor(), turtle.ycor()
    turtle.left(135)
    turtle.forward(10)
    turtle.goto(x,y)
    turtle.right(135)
    turtle.right(135)
    turtle.forward(10)
    turtle.backward(10)
    turtle.left(135)

def draw_bar_graph(f):
    vertical = max(list(f.values()))
    turtle.left(90)
    turtle.forward(vertical*20)
    make_arrow_head()
    turtle.write("Y")
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90)
    turtle.pendown()
    for i in range(len(f)):
        if i == 0:
            turtle.forward(20)
        # turtle.forward(0)
        turtle.left(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.left(90)
        x,y = turtle.xcor(), turtle.ycor()
        turtle.penup()
        turtle.goto(x-30,y-20)
        turtle.write(list(f.keys())[i])
        turtle.goto(x,y)
        turtle.pendown()

    turtle.forward(20)
    make_arrow_head()
    turtle.write("X")
    turtle.goto(0,0)

def main():
    ls = [1, 2, 2, 1, 3, 4 ,5, 6, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4]
    f = freq_distri(ls)
    draw_bar_graph(f)
    turtle.done()

main()
