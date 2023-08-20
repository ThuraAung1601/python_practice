'''
No.5
Write a Python program which asks the user to input an integer amount of money (in Baht).
The program then calculates a combination of bank notes and coins whose sum of values equals to
the user's input. We assume that the following bank notes and coins are available (in unlimited quantity):
    1000-Baht notes
    500-Baht notes
    100-Baht notes 
    50-Baht notes
    20-Baht notes
    10-Baht coins
    5-Baht coins
    2-Baht coins
    1-Baht coins
The program should find the combination with the least number of notes and coins.
'''
notes_and_coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def bank_note_convert(amount):
    result = []
    for i in notes_and_coins:
        quotient = amount//i
        amount = amount % i
        result.append(quotient)
    return result

def main():
    input_money = int(input("Input your amount of money: "))
    result = bank_note_convert(input_money)
    index = 0
    while index < len(notes_and_coins) :
        bath_type = "Baht notes"
        if notes_and_coins[index] <= 10 :
            bath_type = "Baht coins"
        if result[index] != 0 :
            print(f"{notes_and_coins[index]}-{bath_type} : {result[index]}")
        index += 1

main()