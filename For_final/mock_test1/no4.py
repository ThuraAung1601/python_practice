'''
Define a class EWallet which a person can use to keep his/her (electronic) money.
The owner can put money into and take money out from the e-wallet. For each e-wallet, it must have
an owner and maximum money amount the wallet can keep. The owner can check the current money amount
in his/her wallet any time.
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
    
wallet = EWallet("Mg Mg", 100, 230)
wallet.check_current_amount()

print("added 150")
wallet.put_money(150)
wallet.check_current_amount()

print("added 110")
wallet.put_money(110)
wallet.check_current_amount()

print("take 10")
wallet.take_money(10)
wallet.check_current_amount()

print("take 210")
wallet.take_money(210)
wallet.check_current_amount()