'''
No.4
Write a recursive program to solve the tower of Hanoi and
draw an animation of it.
'''
import turtle
import time

class TowerOfHanoi:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)
        self.screen.title('Tower of Hanoi')
        turtle.tracer(0)

        self.base = self.create_base()
        self.pins = self.create_pins()
        self.discs = self.create_discs()
        self.animate_hanoi(5, 'A', 'B', 'C')

    def create_base(self):
        base = turtle.Turtle()
        base.color('grey')
        base.shape('square')
        base.up()
        base.goto(0, -200)
        base.shapesize(1, 35)
        return base

    def create_pins(self):
        pins = {}
        pins['A'] = self.create_pin(-200, 5)
        pins['B'] = self.create_pin(0)
        pins['C'] = self.create_pin(200)
        return pins

    def create_pin(self, xpos, count=0):
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

    def create_discs(self):
        discs = []
        discs.append(self.create_disc(-200, -180, 10, 'orange'))
        discs.append(self.create_disc(-200, -160, 8, 'blue'))
        discs.append(self.create_disc(-200, -140, 6, 'red'))
        discs.append(self.create_disc(-200, -120, 4, 'yellow'))
        discs.append(self.create_disc(-200, -100, 2, 'green'))
        self.pins['A'].discs = discs
        return discs

    def create_disc(self, xpos, ypos, size, color):
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

    def move_disc(self, disc, pin):
        while disc.ycor() < 100:
            disc.goto(disc.xcor(), disc.ycor() + 5)
            turtle.update()
        disc.goto(pin.xcor(), 100)
        turtle.update()
        while disc.ycor() > pin.pos_list[pin.count]:
            disc.goto(disc.xcor(), disc.ycor() - 5)
            turtle.update()
        time.sleep(0.01)

    def move(self, f, t):
        print(f'Move disc from {f} to {t}!')
        start_pin = self.pins[f]
        pin = self.pins[t]

        top_disc = start_pin.discs[-1]
        self.move_disc(top_disc, pin)

        start_pin.count -= 1
        start_pin.discs.pop()
        pin.count += 1
        pin.discs.append(top_disc)

    def hanoi(self, n, f, h, t):
        if n == 0:
            pass
        else:
            self.hanoi(n - 1, f, t, h)
            self.move(f, t)
            self.hanoi(n - 1, h, f, t)

    def animate_hanoi(self, n, f, h, t):
        turtle.update()
        self.hanoi(n, f, h, t)

        turtle.done()

if __name__ == '__main__':
    TowerOfHanoi()
