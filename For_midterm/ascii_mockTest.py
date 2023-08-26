while True:
    char = input("Please enter a character: ")
    ascii = ord(char)
    if ascii == 0x2e:
        break
    elif ascii >= 0x30 and ascii <= 0x39:
        print("{} is a numeric character.".format(char))
    elif ascii >= 0x41 and ascii <= 0x5a:
        print("{} is a capital letter.".format(char))
    elif ascii >= 0x61 and ascii <= 0x7a:
        print("{} is a small-case letter.".format(char))
    else:
        print("{} is a special character.".format(char))
print("Good Bye.")