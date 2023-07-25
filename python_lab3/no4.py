char = input("Please enter a character:")

ascii = ord(char)
ascii_hex = format(ascii,"x")

if ascii_hex >= '30' and ascii_hex <= '39':
    print("{} is a numeric character.".format(char))
#elif ascii >= 0x41 and ascii <= 0x5a:
elif ascii_hex >= '41' and ascii_hex <= '5a':
    print("{} is a capital letter and its small-case letter is {}".format(char,char.lower()))
elif ascii_hex >= '61' and ascii_hex <= '7a':
    print("{} is a small-case letter and its capital letter is {}".format(char,char.upper()))
else:
    print("{} is a special character.".format(char))
