phone_book = {}

while True: 
    print("Phonebook Manager\n\
    Press \"+\" to add a new contact.\n\
    Press \"-\" to delete a new contact.\n\
    Press \"f\" to find a new contact.\n\
    Press \"p\" to print all contacts.\n\
    Press \"q\" to quit the program.")

    operation = input()

    if operation == "+":
        name = input("Enter name to add: ")
        number = input("Enter number: ")
        phone_book[name] = number

    elif operation == "-":
        name = input("Enter name to remove: ")
        if name in phone_book:
            phone_book.pop(name)
        else:
            print(f"{name} is not in the phone_book")

    elif operation == "f":
        name = input("Enter name to find: ")
        if name in phone_book:
            number = phone_book[name]
            print(f"THe Phone number is {number}.")
        else:
            print(f"{name} is not in the phone_book")

    elif operation == "p":
        print(phone_book)

    elif operation == "q":
        break

    