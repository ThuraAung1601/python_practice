'''
Define a class SmartEWallet as a sub-class of EWallet. The class SmartEWallet is different from its
super class as follows:
1. an object of SmartEWallet stores sequentially historical activities of putting money in and
taking money out from this smart e-wallet.
2. the owner can set the maximum money amount for every taking out of money from his/her wallet.
3. the owner can view all of the historical activities stated in 1.
'''
class EWallet(object):
    def __init__(self, owner, amount, maximum):
        self.owner = owner
        self.amount = amount
        self.maximum = maximum
    def put_money(self, amount):
        self.amount += amount
        if self.amount > self.maximum:
            self.amount -= amount
            print("Limit is full to put.")
        return self.amount
    def take_money(self, amount):
        self.amount -= amount
        if self.amount < 0:
            self.amount += amount
            print("The amount is insufficient to take out.")
        return self.amount
    def check_current_amount(self):
        print(self.amount)

class SmartEWallet(EWallet):
    def __init__(self, owner, amount, maximum, history={}):
        super().__init__(owner, amount, maximum)
        self.history = history
    def take_money(self, amount, maximum):
        if amount > maximum:
            print("Cannot take out. Pass the maximum limit to take out.")
        else:
            self.amount = super().take_money(amount)
            self.history[f"Take out {amount}"] = self.amount
        return self.amount
    def put_money(self, amount):
        self.amount = super().put_money(amount)
        self.history[f"Put into {amount}"] = self.amount
        return self.amount
    def view_activities(self):
        print(self.history)

wallet = SmartEWallet("Mg Mg", 200, 230)
print("current")
wallet.check_current_amount()

print("take out 100")
wallet.take_money(100, 120)
wallet.check_current_amount()

print("take out 10")
wallet.take_money(100, 10)
wallet.check_current_amount()

print("add 100")
wallet.put_money(100)
wallet.check_current_amount()

wallet.view_activities()