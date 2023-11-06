'''
Write a Python program using polymorphism to calculate 
cost of items you purchased from a department store.
Sale_item and Food are abstract classes whose concrete classes
are Book, Appliance, Itemized_food and Measured_food.

Itemized_food is priced by items and Measured_food is priced according to its weight. 
A price of a Book is given 15% reduction from its price printed on the cover. 
Food and a Book do not have VAT on top of their prices, 
but an Appliance has VAT 7% on top of the price.

5(a): Define the abstract classes Sale_item and Food. 
Also define the concrete classes - Book, Appliance, Itemized_food and measured_food.
5(b): Write the main program to calculate the total cost of a list of the following 
purchased items:
    • vegetable oil 2 bottles (an Itemized_food), each bottle costs 40 Bahts
    • mango 1.8 Kilograms (Measured_food), each Kilograms cost 70 Bahts
    • one Python book costs 200 Bahts
    • one rice cooker (an Appliance) costs 1,200 Bahts
'''
from abc import ABC, abstractmethod
class Sale_item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def calculate_cost(self):
        pass

class Food(Sale_item, ABC):
    def __init__(self, name, price):
        super().__init__(name, price)
    @abstractmethod
    def calculate_cost(self):
        pass

class Itemized_food(Food):
    def __init__(self, name, price, item):
        super().__init__(name, price)
        self.item = item
    def calculate_cost(self):
        return self.price * self.item
    
class Measured_food(Food):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    def calculate_cost(self):
        return self.price * self.weight

class Book(Sale_item):
    def __init__(self, name, price, discount, amount):
        super().__init__(name, price)
        self.discount = discount
        self.amount = amount
    def calculate_cost(self):
        return self.price * (self.amount * ((100 - self.discount)/100))
    
class Appliance(Sale_item):
    def __init__(self, name, price, top, amount):
        super().__init__(name, price)
        self.top = top
        self.amount = amount
    def calculate_cost(self):
        return self.price * (self.amount * ((100 + self.top)/100))
    
    
vegtable = Itemized_food("Vegetable", 40, 2)
mango = Measured_food("Mango", 70, 1.8)
pythonbook = Book("Python", 200, 15, 1)
ricecooker = Appliance("Rice cooker", 1200, 7, 1)

purchased = [vegtable, mango, pythonbook, ricecooker]

for item in purchased:
    print(item.name, item.calculate_cost())
