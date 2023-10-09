import turtle
import math

def distance(x1, y1, x2, y2):
    '''
    Euclidean distance: the distance between two points
    '''
    return math.sqrt(((x1-x2)**2) + (y1-y2)**2) 

class Robot(object):
    def __init__(self, x=100, y=100, health=100, energy=100):
        self.x = x
        self.y = y
        self.health = health
        self.energy = energy

    def move(self, newX, newY):
        if self.energy > 0:
            self.x = newX
            self.y = newY
            self.energy -= 10
        else:
            pass
    
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.write(f"({self.x}, {self.y})")
        turtle.goto(self.x, self.y-30)
        turtle.pendown()
        turtle.circle(30)
    
    def displayStatus(self):
        return f"x = {self.x}, y = {self.y}, health = {self.health}, energy = {self.energy}"

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinates: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()
    def heal(self, r):
        if self.energy >= 20 and distance(self.x, self.y, r.x, r.y) <= 10:
            self.energy -= 20
            r.health += 10
        else:
            print("Distance out of range")
            pass
        
    def command(self, robotList):
        print("==== Robot ====")
        i = 0
        for robot in robotList:
            print(i, ":", robot.displayStatus())
            i += 1
        print("================")
        command = input("Do you want to move(m) or heal(h) other robot: ")
        if command == 'm':
            super().command(robotList)
        elif command == 'h':
            choice = int(input("Enter ID of robot to heal:"))
            self.heal(robotList[choice])       

class StrikerBot(Robot):
    def __init__(self, missile=5):
        super().__init__()
        self.missle = missile

    def strike(self, r):
        if self.energy >= 20 and self.missle > 0 and distance(self.x, self.y, r.x, r.y) <= 10:
            self.energy -= 20
            self.missle -= 1
            r.health -= 50
        else:
            print("Distance out of range")
            pass
        
    def displayStatus(self):
        return super().displayStatus() + f" missle = {self.missle}"
    
    def command(self, robotList):
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, ":", robot.displayStatus())
            i += 1
        print("=================")
        command = input("Do you want to move(m) or strike(s) other robot: ")
        if command == 'm':
            super().command(robotList)
        elif command == 's':
            choice = int(input("Enter ID of robot to strike:"))
            self.strike(robotList[choice])        

def RobotBattle():
    robotList = []
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, ":", robot.displayStatus())
            i += 1
        print("=================")
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit, Robot ID for operation: ")
        if choice == 'q':
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikeBot: ")
            if robotType == 'r':
                newRobot = Robot()
            elif robotType == 'm':
                newRobot = MedicBot()
            elif robotType == 's':
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)    
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

RobotBattle()
