'''
Write a program that ask the user to put 24-hour format and
print it out in 12-hour format.
'''
hr = int(input("Hours: "))
minu = int(input("Minutes: "))
sec = int(input("Seconds: "))
if hr <= 12 and (minu > 0 or sec > 0): 
    twelve_hr = hr
    am_pm = "AM"
else: 
    twelve_hr = abs(hr-12)
    am_pm = "PM"
print(f"Time you just entered in 12 hour format is {twelve_hr:02d}:{minu:02d}:{sec:02d} {am_pm}.")