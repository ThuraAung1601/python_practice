class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def print_out(self):
        return f"{self.hr:02}:{self.min:02}:{self.sec:02}"

time1 = Time(9, 30, 0)
print(time1.print_out())