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

# ----------------------------------------------------------------


'''
No.2
Write a Python function to take a month of year 2023 as its argument and
it draws the calender for that month in the following form.
For example, calender_of_2023(8)
'''
import turtle

months_31 = [1, 3, 5, 7, 8, 10, 12]
week_days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

calendar_width = 350 
calendar_high = 200
box_width = calendar_width / 7
box_high = calendar_high / 7

turtle.tracer(0)
turtle.penup()
turtle.goto(-380,280)
turtle.pendown()

def calculate_first_day_of_month(month) :
    month = month -1
    first_day_of_month = 0
    for i in range(1, 13) :
        if i in months_31 :
            for k in range(0, 31):
                first_day_of_month += 1
                if first_day_of_month > 7 :
                    first_day_of_month = 1
        elif i == 2 :
            for k in range(0, 28):
                first_day_of_month += 1
                if first_day_of_month > 7 :
                    first_day_of_month = 1
        else :
            for k in range(0, 30):
                first_day_of_month += 1
                if first_day_of_month > 7 :
                    first_day_of_month = 1
        if month == i :
            return first_day_of_month
        
def draw_box(text, write= True) :
    turtle.pendown()
    turtle.forward(box_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    turtle.forward(box_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)

    t_x = turtle.xcor()
    t_y = turtle.ycor()

    if write : 
        turtle.penup()
        turtle.goto(t_x+ 15, t_y - box_high)
        turtle.pendown()
        turtle.write(text)

    turtle.penup()
    turtle.goto(t_x, t_y)
    turtle.forward(box_width)
    
def calender_of_2023(month) :
    first_day = calculate_first_day_of_month(month)

    num_of_days = 0
    if month in months_31 :
        num_of_days = 31
    elif month == 2 :
        num_of_days = 28
    else :
        num_of_days = 30

    turtle.speed(0)
    turtle.forward(calendar_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)
    turtle.forward(calendar_width)
    turtle.right(90)
    turtle.forward(box_high)
    turtle.right(90)

    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() - box_high)
    turtle.pendown()
    turtle.forward(calendar_width)
    turtle.penup()
    turtle.backward(calendar_width)

    t_x = turtle.xcor()
    t_y = turtle.ycor()

    turtle.goto(turtle.xcor() + calendar_width / 2, turtle.ycor() + box_high/4)
    turtle.pendown()
    turtle.write(f"{month_names[month -1]} 2023")
    turtle.penup()
    turtle.goto(t_x, t_y)

    for wk_day in week_days :
        draw_box(wk_day)
    turtle.penup()
    turtle.goto(t_x, t_y - box_high)

    day_count = 0
    for row in range (1, 9) :
        t_x = turtle.xcor()
        t_y = turtle.ycor()

        for col in range(1, 8) :
            write = False
            if day_count == 0 :
                if col == first_day:
                    write = True
                    day_count += 1
            elif day_count < num_of_days :
                write = True
                day_count += 1
            
            draw_box(day_count, write)
        turtle.penup()
        turtle.goto(t_x, t_y - box_high)

        if day_count >= num_of_days :
            break

    turtle.done()


# calender_of_2023(8)
def main():
    ch = ''
    while ch != 'q' or ch != 'Q':
        month = int(input("Enter month:"))
        if month <= 0 or month > 12:
            ch = input("Month input is not valid. Should be in range 1-12.\n Try again(a|A). or Quit(q|Q).")
        else: 
            calender_of_2023(month)
            break

main()

# ------------------------------------------------------

'''
No.4
Write a Python program which asks for an integer from the user.
If the input is in the range 0 - 999, the program outputs the English pronunciation
of that number; otherwise the program outputs "I don't know".
'''
def num2word(input_num):
    english_megas = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion"]
    english_units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    english_tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    english_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    words = []

    hundreds = input_num // 100 % 10
    tens = input_num // 10 % 10
    units = input_num % 10

    if hundreds > 0:
        words.extend([english_units[hundreds], "hundred"])

    if tens == 1:
        words.append(english_teens[units])
    else:
        if units > 0:
            word = f"{english_tens[tens]}-{english_units[units]}"
            words.append(word)
        else:
            words.append(english_tens[tens])
            
    result = " ".join(words)
    return result

def main():
    num = int(input("Enter a number range 0-999: "))
    if num < 0 or num > 999:
        print("I don't know.")
    else: print(num2word(num))

main()

# -------------------------------------------------------------

'''
No.5
Write a Python program which asks the user to input an integer amount of money (in Baht).
The program then calculates a combination of bank notes and coins whose sum of values equals to
the user's input. We assume that the following bank notes and coins are available (in unlimited quantity):
    1000-Baht notes
    500-Baht notes
    100-Baht notes 
    50-Baht notes
    20-Baht notes
    10-Baht coins
    5-Baht coins
    2-Baht coins
    1-Baht coins
The program should find the combination with the least number of notes and coins.
'''
notes_and_coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def bank_note_convert(amount):
    result = []
    for i in notes_and_coins:
        quotient = amount//i
        amount = amount % i
        result.append(quotient)
    return result

def main():
    input_money = int(input("Input your amount of money: "))
    result = bank_note_convert(input_money)
    index = 0
    while index < len(notes_and_coins) :
        bath_type = "Baht notes"
        if notes_and_coins[index] <= 10 :
            bath_type = "Baht coins"
        if result[index] != 0 :
            print(f"{notes_and_coins[index]}-{bath_type} : {result[index]}")
        index += 1

main()

# --------------------------------------------------------------

'''
No.6 
Write a function to return an integer 
whose digits are in the reversed orders of the given integer.
For example, reverse(3456) returns 6543
'''

def reverse(num):
    result_str = str(num)[::-1]
    result = int(result_str)
    return result

def main():
    num = int(input("Enter a number:"))
    print(reverse(num))

main()