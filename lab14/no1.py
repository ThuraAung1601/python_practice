import pickle
from tkinter import filedialog
import os.path

class SpecialError(Exception):
    pass

phonebook = {}

def check_file_exist(filepath):
    if os.path.isfile(filepath):
        raise SpecialError
    
def check_number_valid(number):
    if not number.isdigit():
        raise SpecialError

while True:
    print("Phonebook Manager")
    print("Press '+' to add a new contact")
    print("Press '-' to delete a contact")
    print("Press 'f' to find a contact")
    print("Press 's' to save all contact to a file")
    print("Press 'l' to load previous saved contact from a file")
    print("Press 'p' to print all contacts")
    print("Press 'q' to quit")
    print("\n=====================================")
    choice = input("\nEnter your choice: ")
    
    if choice == "+":
        name = input("Enter name: ")
        number = input("Enter number: ")
        try:
            check_number_valid(number)
            if name in phonebook.keys():
                print("\nContact already exists\n")
            else:
                phonebook[name] = number
                print(f"\n{name} has been added to the phonebook with number {number}\n")
        except SpecialError:
            print("\nInvalid number\n")
    elif choice == "-":
        name = input("Enter name: ")
        if phonebook.keys().__contains__(name):
            print(f"\nPhone number of {name} ({phonebook[name]}) has been deleted\n")
            del phonebook[name]
        else:
            print(f"\n{name} is not in the phonebook\n")
    elif choice == "f":
        name = input("Enter name: ")
        if phonebook.keys().__contains__(name):
            print(f"\nPhone number of {name} is {phonebook[name]}\n")
        else:
            print(f"\n{name} is not in the phonebook\n")
    elif choice == "p":
        print()
        for name, number in phonebook.items():
            print(f"{name}: {number}")
            
        print()
    elif choice == "s":
        filepath = filedialog.asksaveasfilename(filetypes=[('All Files', '*.*')], title="Save Phonebook")
        if filepath is None:
            print("\nFile not saved\n")
        else:
            try:
                check_file_exist(filepath)
                file = open(filepath, "wb")
                pickle.dump(phonebook, file)
                file.close()
                print("\nPhonebook saved\n")
            except SpecialError:
                print("\nFile already exists\n")
                    
        
    elif choice == "l":
        filepath = filedialog.askopenfile(filetypes=[('All Files', '*.*')], title="Load Phonebook")
        if filepath is None:
            print("\nFile not Load\n")
        else:
            file = open(filepath.name, "rb")
            load = pickle.load(file)
            print("Loaded content: ")
            
            for name, number in load.items():
                print(f"{name}: {number}")
                phonebook[name] = number
            
            print("\nPhonebook has been loaded\n")
    elif choice == "q":
        break
    else:
        print("\nInvalid\n")