'''
No.1
Write a Python function to convert a time of the 24 hour format 
into the 12 hour format.
For example, time24hourTo12hour("23:24") => 11:24 PM.
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