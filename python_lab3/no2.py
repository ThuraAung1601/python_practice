num = eval(input("Enter a number:"))

if isinstance(num, float):
    ques = input("Display the number in float (F) or scientific format (S): ")
    if ques == "F" or ques == "f":
        print("Your float number is {}".format(num))
    elif ques == "S" or ques == "s":
        print("Your number in scientific format is {}".format(format(num,"5.2e")))
    else:
        print("Invalid choice. Your number is {}".format(num))

elif isinstance(num, int):
    ques = input("Display your integer in Binary(B), Octal(O), Hexadecimal(H) or Decimal(D): ")
    if ques == "D" or ques == "d":
        print("Your integer number in decimal is {}".format(num))
    elif ques == "B" or ques == "b":
        print("Your number in binary format is {}".format(format(num,"b")))
    elif ques == "O" or ques == "o":
        print("Your number in Octal format is {}".format(format(num,"o")))
    elif ques == "H" or ques == "h":
        print("Your number in Hexadecimal format is {}".format(format(num,"x")))
    else:
        print("Invalid choice. Your number is {}".format(num))

else:
    print("Invalid input. Please try with numbers.")
