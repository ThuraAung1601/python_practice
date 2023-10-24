'''
Define a SavingAccount class which has the following properties and methods:
Properties
    - bank_name: the name of the bank who creates the account
    - acc_name: the name and surnname of the account owner
    - acc_id: the account id
    - balance: the current balance of the account
    - transaction_history: transaction history of the account (stored in a list)
Methods
    - deposit(money, person, date): deposit money by person to the account on date
    - withdraw(money, person, date): withdraw money by person from the account on date
    - get_balance(): get the current balance
    - print_statement(): print the statement according to transaction_history

Define a OverDrawnAccount as a sub-class of SavingAccount class. An overdrawn account is 
different from a saving account very little, in that a saving account cannot have a negative balance
whilst an overdrawn account can have a negative balance but it does not exceed the over drawn 
limit. Please define necessary properties and methods for this sub-class.
'''

class SavingAccount(object):
    def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history=[]):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = transaction_history
    def deposit(self, money, person, date):
        self.balance += money
        self.transaction_history.append(["Deposits", money, person, date])
    def withdraw(self, money, person, date):
        if self.balance < money:
            print("Insufficient amount")
        self.balance -= money
        self.transaction_history.append(["Withdraw", money, person, date])
    def get_balance(self):
        return self.balance
    def print_statement(self):
        print(f"Current balance is {self.balance}")
        print(f"The Transaction History is: \n {self.transaction_history}")
    
class OverDrawnAccount(SavingAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, overdrawn_limit, transaction_history=[]):
        super().__init__(bank_name, acc_name, acc_id, balance, transaction_history)
        self.overdrawn_limit = overdrawn_limit
    def withdraw(self, money, person, date):
        if self.overdrawn_limit < money:
            print("Insufficient amount")
        self.balance -= money
        self.transaction_history.append(["Overdrawn Withdraw", money, person, date])

overdrawn = OverDrawnAccount("Overdrawn", "John", "123456", 100, 500)

overdrawn.deposit(100, "John", "2020-01-01")
overdrawn.withdraw(200, "John", "2020-01-02")
overdrawn.withdraw(502, "John", "2020-01-03")
overdrawn.print_statement()