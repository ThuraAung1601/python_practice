'''
No.4
Write a recursive program to solve the tower of Hanoi and
draw an animation of it.
'''
import turtle
import time

turtle.Screen()
turtle.setup(800, 600)
turtle.title('Tower of Hanoi')
turtle.tracer(0)

base = turtle.Turtle()
base.color('grey')
base.shape('square')
base.up()
base.goto(0, -200)
base.shapesize(1, 35)

def create_pin(xpos, count=0):
    pin = turtle.Turtle()
    pin.shape('square')
    pin.xpos = xpos
    pin.up()
    pin.color('grey')
    pin.shapesize(10, 1)
    pin.goto(pin.xpos, -100)
    pin.count = count
    pin.pos_list = [-180, -160, -140, -120, -100]
    pin.discs = []
    return pin

def create_disc(xpos, ypos, size, color):
    disc = turtle.Turtle()
    disc.shape('square')
    disc.xpos = xpos
    disc.ypos = ypos
    disc.size = size
    disc.color(color)
    disc.up()
    disc.shapesize(1, size)
    disc.goto(disc.xpos, disc.ypos)
    return disc

def move_disc(disc, pin):
    while disc.ycor() < 100:
        disc.goto(disc.xcor(), disc.ycor() + 5)
        turtle.update()
    disc.goto(pin.xcor(), 100)
    turtle.update()
    while disc.ycor() > pin.pos_list[pin.count]:
        disc.goto(disc.xcor(), disc.ycor() - 5)
        turtle.update()
    time.sleep(0.01)

def move(f, t, pins):
    print(f'Move disc from {f} to {t}!')
    start_pin = pins[f]
    pin = pins[t]

    top_disc = start_pin.discs[-1]
    move_disc(top_disc, pin)

    start_pin.count -= 1
    start_pin.discs.pop()
    pin.count += 1
    pin.discs.append(top_disc)

def hanoi(n, f, h, t, pins):
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, t, h, pins)
        move(f, t, pins)
        hanoi(n - 1, h, f, t, pins)

pins = {
    'A': create_pin(-200, 5),
    'B': create_pin(0),
    'C': create_pin(200)
}

disc1 = create_disc(-200, -180, 10, 'orange')
disc2 = create_disc(-200, -160, 8, 'blue')
disc3 = create_disc(-200, -140, 6, 'red')
# disc4 = create_disc(-200, -120, 4, 'yellow')
# disc5 = create_disc(-200, -100, 2, 'green')

pins['A'].discs = [disc1, disc2, disc3]

hanoi(3, 'A', 'B', 'C', pins)

turtle.done()