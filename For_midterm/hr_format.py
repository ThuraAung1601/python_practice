'''
Write a program that ask the user to put 24-hour format and
print it out in 12-hour format.
'''
def time24hourTo12hour(twenty_four_hr_format):
    twenty_four_hr_format = twenty_four_hr_format.split(":")
    hour = int(twenty_four_hr_format[0])
    minute = int(twenty_four_hr_format[1])
    if hour <= 12 and minute > 0: 
        twelve_hr = hour
        am_pm = "AM"
    else: 
        twelve_hr = abs(hour-12)
        am_pm = "PM"
    twelve_hr_format = f"Time you just entered in 12 hour format is {twelve_hr:02d}:{minute:02d} {am_pm}."
    return twelve_hr_format

print(time24hourTo12hour("23:24"))
