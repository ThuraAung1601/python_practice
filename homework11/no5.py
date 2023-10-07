from abc import ABC, abstractmethod

class Goods(object):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def getCost(self):
        pass

class StationaryGood(Goods):
    def __init__(self, type, quantity, price):
        self.type = type
        self.quantity = quantity
        self.price = price
    def getCost(self):
        return self.quantity * self.price
    
class Magazine(Goods):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def getCost(self):
        return self.quantity * self.price
    
class Book(Goods):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def getCost(self):
        self.discount_rate = 0.9 # 10% discound
        return self.quantity * self.price * self.discount_rate
    
class Ribbon(Goods):
    def __init__(self, color, metre):
        self.color = color
        self.metre = metre
        self.price = 5 # 5 bhats per 1 metre
    def getCost(self):
        return self.metre * self.price
    
basket = [StationaryGood("Notebook", 1, 35),
          Magazine("WIRED", 1, 230),
          Book("Adventure of a Mathematician", 1, 450),
          Ribbon("Blue", 23)]

def getTotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.getCost()
    return total_cost

print(getTotalCost(basket)) #Output: 785.0