def integer_to_en_us(input_num):
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
        quit()
    print(integer_to_en_us(num))

main()
