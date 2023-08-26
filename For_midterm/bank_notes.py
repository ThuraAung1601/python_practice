notes_and_coins = [1000, 500, 100]

def bank_note_convert(amount):
    result = []
    for i in notes_and_coins:
        quotient = amount//i
        amount = amount % i
        result.append(quotient)
    return result

def main():
    input_money = int(input("How much do you want to withdraw: "))
    result = bank_note_convert(input_money)
    index = 0
    while index < len(notes_and_coins) :
        if result[index] != 0 :
            print(f"You get {result[index]} notes of {notes_and_coins[index]}.")
        index += 1

main()
