def check_it(ascii):
    if ascii >= 0x30 and ascii <= 0x39:
        result = "{} is a numeric character.".format(c)
    elif ascii >= 0x41 and ascii <= 0x5a:
        result = "{} is a capital letter and its small-case letter is {}".format(c, c.lower())
    elif ascii >= 0x61 and ascii <= 0x7a:
        result = "{} is a small-case letter and its capital letter is {}".format(c, c.upper())
    else:
        result = "{} is a special character.".format(c)
    return result

char = input("Please enter a character:")
while char != "\t":
    for c in char:
        output = check_it(ord(c))
        print(output)
    char = input("Please enter a character:")

print("See You Tomorrow")
