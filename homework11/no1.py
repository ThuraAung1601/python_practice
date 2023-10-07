class Clock(object):
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    def run(self):
        self.ss += 1
        if self.ss >= 60:
            self.ss = 0
            self.mm += 1
        if self.mm >= 60:
            self.mm = 0
            self.hh += 1
        if self.hh >= 24:
            self.hh = 0
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s

class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_hh, alarm_mm, alarm_ss, alarm_on_off):
        super().__init__(hh, mm, ss)
        self.alarm_hh = alarm_hh
        self.alarm_mm = alarm_mm
        self.alarm_ss = alarm_ss
        self.alarm_on_off = alarm_on_off
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
    def alarm_on(self):
        self.alarm_on_off = True
    def alarm_off(self):
        self.alarm_on_off = False
    def run(self):
        while True:
            super().run()
            if self.alarm_on_off:
                if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                    print("This is alarm time !!!")
                    break

clock = AlarmClock(12, 21, 36, 14, 32, 56, True)
clock.run()