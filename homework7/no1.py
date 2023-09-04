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
        self.hour = newHour
        self.minute = newMinute
        self.second = newSecond
    def get_hour(self):
        return self.hour
    def get_minute(self):
        return self.minute
    def get_second(self):
        return self.second
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
        if self.hour >= 12:
            self.hour = self.hour - 12
            am_pm = "PM"
        else:
             am_pm = "AM"
        print(f"Your current time is {self.hour:02d}:{self.minute:02d}:{self.second:02d} {am_pm}.")

c = Clock(0,0,0)
c.display()
c.set_time(22,30,5)
current_hour = c.get_hour()
print(current_hour)
c.set_time(23,24,50)
current_hour = c.get_hour()
print(current_hour)
current_minute = c.get_minute()
print(current_minute)
c.display()