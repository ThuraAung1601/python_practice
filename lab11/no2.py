# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))

# def factorial1(n):
#     num = 1
#     for i in range(2, n+1):
#         num *= i
#     print(num)

# factorial1(4)

class Calculator:
    def __init__(self, accu):
        self.accumulator = accu
    def set_accumulator(self, accu):
        self.accumulator = accu
    def get_accumulator(self):
        return self.accumulator
    def add(self, num):
        self.accumulator += num
    def subtract(self, num):
        self.accumulator -= num
    def multiply(self, num):
        self.accumulator *= num
    def divide(self, num):
        if num == 0:
            # raise ZeroDivisionError
            print("Cannot divide by zero")
        else:
            self.accumulator /= num

class SciCalculator(Calculator):
    def __init__(self, accu):
        super().__init__(accu)
    def square(self):
        self.accumulator *= self.accumulator
    def expo(self, num):
        self.accumulator **= num
    def factorial(self):
        result = 1
        for i in range(2, int(self.accumulator)+1):
            result *= i
        self.accumulator = result
    def print_result(self):
        print(f"Result: {self.accumulator:.02e}")

cal = Calculator(100)
cal.set_accumulator(100)
print(cal.get_accumulator())

cal.add(10)
print(cal.get_accumulator())

cal.subtract(10)
print(cal.get_accumulator())

cal.multiply(10)
print(cal.get_accumulator())

cal.divide(10)
print(cal.get_accumulator())

sci = SciCalculator(4)
sci.set_accumulator(4)
sci.expo(3)
sci.print_result()

sci.divide(25)
print(sci.get_accumulator())
sci.factorial()
print(sci.get_accumulator())

sci.divide(0)
print(sci.get_accumulator())
sci.print_result()

sci.set_accumulator(100)
sci.print_result()