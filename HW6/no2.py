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