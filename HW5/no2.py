import turtle

day = ["Su","Mo","Tu","We","Th","Fr","Sa"]
month = [31,28,31,30,31,30,31,31,30,31,30,31]
date, per_week = 0, 1
# turtle.speed(0)
turtle.tracer(0)
turtle.penup()
turtle.goto(-380,280)
turtle.pendown()

def text_write(msg):
    turtle.forward(5)
    turtle.write(msg)
    turtle.backward(5)

def draw_box(N):
    counter = 0
    while counter < N:
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        counter += 1

def draw_wide(fwd):
    turtle.left(90)
    turtle.forward(fwd)
    turtle.left(90)

x = 0
while x < 12:
    if x != 0 and x%4 == 0:
       turtle.penup()
       turtle.goto(turtle.xcor() + 280, 280)
       turtle.pendown()

    y = 0
    while y < 7:
        text_write(day[y])
        draw_box(2) # 2 2-sided pairs
        turtle.forward(25)
        y += 1

    draw_wide(30)
    turtle.forward(175)
    draw_wide(15)
    text_write(f"Month#{x+1}")
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    
    date = month[x]
    while date > 0:
        a = 1
        while a < 8:
            if a == per_week and date > 0:
                date -= 1
                turtle.forward(5)
                turtle.write(month[x] -date)
                turtle.back(5)
                draw_box(2)
                turtle.forward(25)
                print("perweek",per_week)
                if per_week == 7:
                    per_week = 1
                else:
                    per_week += 1
            else:
                # Empty box
                draw_box(2)
                turtle.forward(25)
            a += 1
        if date > 0:
            turtle.back(175)
            turtle.right(90)
            turtle.forward(15)
            turtle.left(90)
        else:
            turtle.back(175)
            turtle.right(90)
            turtle.penup()
            turtle.forward(45)
            turtle.pendown()
            turtle.left(90)
    x += 1
turtle.update()
turtle.done()
