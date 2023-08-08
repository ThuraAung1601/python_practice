char = input("Please enter a character:")
char_list = [ c for c in char ]

def check_it(ascii):
    if ascii >= 0x30 and ascii <= 0x39:
        print("{} is a numeric character.".format(c))
    elif ascii >= 0x41 and ascii <= 0x5a:
        print("{} is a capital letter and its small-case letter is {}".format(c,c.lower()))
    elif ascii >= 0x61 and ascii <= 0x7a:
        print("{} is a small-case letter and its capital letter is {}".format(c,c.upper()))
    else:
        print("{} is a special character.".format(c))

while char != "\t":
    for c in char_list:
        check_it(ord(c))
    char = input("Please enter a character:")
    char_list = [ c for c in char ]

print("See You Tomorrow")
