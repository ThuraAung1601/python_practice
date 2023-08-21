'''
No.4
Write a Python program which asks for an integer from the user.
If the input is in the range 0 - 999, the program outputs the English pronunciation
of that number; otherwise the program outputs "I don't know".
'''
def num2word(input_num):
    english_units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    english_tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    english_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    words = []

    hundreds = input_num // 100 % 10
    tens = input_num // 10 % 10
    units = input_num % 10

    if hundreds > 0:
        words.extend([english_units[hundreds], "hundred"])

    if tens == 1:
        words.append(english_teens[units])
    else:
        if units > 0:
            word = f"{english_tens[tens]} {english_units[units]}"
            words.append(word)
        else:
            words.append(english_tens[tens])
            
    result = " ".join(words)
    return result

def main():
    num = int(input("Enter a number range 0-999: "))
    if num < 0 or num > 999:
        print("I don't know.")
    else: print(num2word(num))

main()
