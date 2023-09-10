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

def int2binary_r(num):
    if num == 0:
        return str(num)
    else:
        binary = num % 2
        rest = num // 2
        return int2binary_r(rest) + str(binary)

# print(int2binary(num))
# print(int2binary_r(num))

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

def binary2int_r(binary):
    power = len(binary) - 1
    if len(binary) == 0:
        return 0
    else:
        return int(binary[0])*(2**power) + binary2int_r(binary[1:])

# print(binary2int(num))
# print(binary2int_r(str(num)))

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
