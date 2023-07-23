"""
Program to ask the use to enter four digit integer 
and print out in reverse
"""
four_digit_int = int(input("Enter four digit integer:"))

four_digit_int_string = str(four_digit_int)
four_digit_int_string_reverse = four_digit_int_string[::-1]
print("Your number in reverse is", int(four_digit_int_string_reverse))
