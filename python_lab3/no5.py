char = input("Please enter a character:")
ascii = ord(char)

while char != "\t":
    if ascii >= 0x30 and ascii <= 0x39:
        print("{} is a numeric character.".format(char))
    elif ascii >= 0x41 and ascii <= 0x5a:
        print("{} is a capital letter and its small-case letter is {}".format(char,char.lower()))
    elif ascii >= 0x61 and ascii <= 0x7a:
        print("{} is a small-case letter and its capital letter is {}".format(char,char.upper()))
    else:
        print("{} is a special character.".format(char))
    char = input("Please enter a character:")
    ascii = ord(char)

print("See You Tomorrow")