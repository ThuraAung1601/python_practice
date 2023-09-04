'''
No.1
Define a clock class in python whose properties are hour, minute, second 
and it provide methods to set time get time tick (increment current time by 1 second) 
and display time in am/pm format.
'''
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def set_time(self, newHour, newMinute, newSecond):
        if 0 <= newHour <= 24 and 0 <= newMinute < 60 and 0 <= newSecond < 60:
            self.hour = newHour
            self.minute = newMinute
            self.second = newSecond
            return f"Set Time {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        else:
            return "Invalid time format."
    def get_time(self):
        return self.hour, self.minute, self.second
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.hour = 0
    def display(self):
        am_pm = "AM" if self.hour < 12 else "PM"
        if self.hour == 0:
            hour = 12
        elif self.hour <= 12:
            hour = self.hour
        else:
            hour = self.hour - 12
        print(f"Your current time is {hour:02d}:{self.minute:02d}:{self.second:02d} {am_pm}.")

c = Clock(0,0,0)
c.display()

c.set_time(22,30,5)
current_time = c.get_time()
print(current_time)

c.set_time(23,24,59)
c.display()
c.tick()
c.display()

c.set_time(23,59,59)
c.display()
c.tick()
c.display()

c.set_time(13,59,59)
c.display()
c.tick()
c.display()
