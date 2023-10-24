'''
Write a Python program using polymorphism to calculate cost of a telephone service.
PhoneService is an abstract class whose concrete classes are Post_paid, Pre_paid, Fixed_line and
so on. PhoneService has three properties: phone_no, customer_name, and mm_yyyy (a month of service.)

For each phone service cost, a post-paid service is charged with a fixed cost if the call duration does not 
exceed the monthly allowance (the time limit), any extra minute will be charged with 1 Baht per minute. A pre-paid service
will be charged with 2 Bahts per minute. A fixed-line service will be charged with 3 Bahts per local call.
'''
from abc import ABC, abstractmethod

class PhoneService(ABC):
    def __init__(self, phone_no, customer_name, mm_yyyy):
        self.phone_no = phone_no
        self.customer_name = customer_name
        self.mm_yyyy = mm_yyyy
    @abstractmethod
    def find_cost(self):
        pass

class Post_paid(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, fixed_price, monthly_allowance, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.fixed_price = fixed_price
        self.monthly_allowance = monthly_allowance
        self.call_duration = call_duration
    def find_cost(self):
        if self.call_duration <= self.monthly_allowance:
            return self.fixed_price
        else:
            exceed_time = self.call_duration - self.monthly_allowance
            self.fixed_price += exceed_time * 1
            return self.fixed_price

class Pre_paid(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, call_duration):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.call_duration = call_duration
    def find_cost(self):
        return self.call_duration * 2
    
class Fixed_line(PhoneService):
    def __init__(self, phone_no, customer_name, mm_yyyy, no_local_call):
        super().__init__(phone_no, customer_name, mm_yyyy)
        self.no_local_call = no_local_call
    def find_cost(self):
        return self.no_local_call * 3
    
    
postpaid = Post_paid("080-000-0007", "John English", "09-2021", 800, 1000, 1250)
prepaid = Pre_paid("080-000-0007", "John English", "09-2021", 100)
fixedLine = Fixed_line("080-000-0007", "John English", "09-2021", 200)

print(postpaid.find_cost())
print(prepaid.find_cost())  
print(fixedLine.find_cost())