class BankAccount:
    def __init__(self, bankName, ownerName, accountNumber, currentBalence):
        self.bankName = bankName
        self.ownerName = ownerName
        self.accountNumber = accountNumber
        self.currentBalence = currentBalence
    def deposit(self, amount):
        self.currentBalence += amount
        return self.currentBalence
    def withdraw(self, amount):
        if self.currentBalence < amount:
            print(f"Your current balance is {self.currentBalence}. Not enough to widthdraw {amount}.")
        else:
            self.currentBalence -= amount
            return self.currentBalence
    def current_balance(self):
        return f"Current balance is {self.currentBalence}"

b1 = BankAccount("K-Bank", "Thura Aung", "1234", 3000)
print(b1.current_balance())
b1.deposit(1000)
print(b1.current_balance())
b1.withdraw(500)
print(b1.current_balance())
b1.withdraw(3200)
print(b1.current_balance())
b1.withdraw(500)

        
        
    