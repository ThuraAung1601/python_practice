'''
No.1
The Problem:
We are going to do some conversions, from integer to binary and then
from binary back to integer. It will give us a chance to play with if-elif-else and
while statements, as well as little string slicing.
Task:
Prompt for an integer input, convert the integer to a binary number string 
(there is no type for actual binary numbers so we just represent it as a string).
We then take the string and turn it back into a regular integer.
'''

def int2binary(num):
    binary = ""
    while num > 0:
        if num%2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
    return binary

def binary2int(num):
    binary = str(num)
    integer = 0
    power = 0
    i = len(binary)
    while i >= 0:
        if binary[i-1] == '1':
            integer += 2**power
        power += 1
        i -= 1
    return integer

def main():
    num = int(input("Enter an integer number: "))
    if num == 0:
        print("0")
    elif num < 0:
        print("The number is negative.")
        quit()
    else:
        ch = input("Enter b to get binary and i to get integer:")
        if ch == 'b':
            print(int2binary(num))
        elif ch == 'i':
            print(binary2int(num))

main()

# ---------------------------------------------------------- #

'''
No.2
Write a Python program for reading a string from the user then
printing the frequency distribution of each character occurring
in the string (that is, the percentage of the length of the whole string).
'''
def freq_distro(text):
    freq = {}
    for c in text:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

def main():
    text = input("Enter some text:")
    freq = freq_distro(text)
    # print(freq)
    print("-- Character Frequency Table -")
    for i in freq:
        char_percentage = freq[i] / len(text)
        print("{}{:>10.2%}".format(i, char_percentage))

main()

# ---------------------------------------------------------- #

'''
No.3
Write a Python program for reading a string from the user then drawing a bar graph
for the count of each character occuring in the string using the turtle module.
Note: each bar has the height of 20 times of its character count,
and the height of the vertical axis will be the same as the height of
the tallest bar.
'''
import turtle
def freq_distri(text):
    freq = {}
    for c in text:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def make_arrow_head():
    x,y = turtle.xcor(), turtle.ycor()
    turtle.left(135)
    turtle.forward(10)
    turtle.goto(x,y)
    turtle.right(135)
    turtle.right(135)
    turtle.forward(10)
    turtle.backward(10)
    turtle.left(135)

def draw_bar_graph(f):
    vertical = max(list(f.values()))
    turtle.left(90)
    turtle.forward(vertical*20)
    make_arrow_head()
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90)
    turtle.pendown()
    for i in range(len(f)):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(list(f.values())[i]*20)
        turtle.left(90)
        x,y = turtle.xcor(), turtle.ycor()
        turtle.penup()
        turtle.goto(x-5,y-10)
        turtle.write(list(f.keys())[i])
        turtle.goto(x,y)
        turtle.pendown()

    turtle.forward(20)
    make_arrow_head()
    turtle.goto(0,0)

def main():
    text = input("Enter some text:")
    f = freq_distri(text)
    draw_bar_graph(f)
    turtle.done()

main()

# ---------------------------------------------------------- #

'''
No.4
An ISBN-10 (International Standard Book Number) consists of 10 digits:
d1d2d3d4d5d6d7d8d9d10. The last digit, d10 is checksum, which is calculated
from the other nine digits using the following formula:
d1 x 1 + d2 x 2 + d3 x 3 + d4 x 4 + d5 x 5 + d6 x 6 + d7 x 7 + d8 x 8 + d9 x 9 + d10 x 10
If the checksum is 10, the last digit is denoted as X, according to the ISBN convention. 
Write a program that prompts the user to enter the first 9 digits as a string and 
displays the 10-digit ISBN (including the leading 0).
Your program should read the input as a string.
'''
def isbn10(digits):
    if len(digits) != 9:
        return "The digit input should be 9 digits."
    else:
        num = 0
        for i,c in enumerate(digits):
            num += int(c)*(i+1)
        num = num % 11
        if num  >= 10:
            num = "X"
        else:
            num = str(num)
        digits += num
        return digits

def main():
    nine_digit = input("Enter the first 9 digits of an ISBN-10 as a string: ")
    isbn10_num = isbn10(nine_digit)
    print(isbn10_num)

main()

# ---------------------------------------------------------- #
