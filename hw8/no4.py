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
