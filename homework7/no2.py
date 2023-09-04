'''
No.2
A single-variable polynomial can be represented in Python as a tuple of coefficient.
For example, the polynomial 14+7x-5x^2+18x^5 can be represented as (14, 7, -5, 0, 0, 18).
Define the class Poly which stores a polynomial in variable x represented in tuple
format and provides the following methods:Methods:
- add(p): given a Poly object p, returns the result of adding itself with p
- scalar_multiply(n): given a number n, returns the result of multiply c with
itself
- multiply(p): given a Poly object p, returns the result of multiply itself with p
- power(n): given a natural number n ≥ 0, return the Poly object resulted from
taking the nth-power
- diff(): returns the Poly object resulted from differentiating the stored
polynomial with respect to
- integrate(): returns the Poly object resulted from integrating the stored
polynomial with respect to × (the constants resulted from the integration can
be assumed to be 0)
- eval(n): given a number n, evaluate the polynomial with x = n
- print(): print out the stored polynomial in a pretty format (e.g. 14 + 7x - 5×^2
+ 18×^5)
The class may contain additional properties and methods not described here.
The construction of an object of class Poly should accept a tuple representing a
polynomial and store it in, the object.
'''
class Poly :
    def __init__(self, coefficients):
        self.x = coefficients
    def add(self, p) :
        larger_poly = self.x
        smaller_poly = p.x
        if len(p.x) >= len(self.x) :
            larger_poly = p.x
            smaller_poly = self.x
        larger_poly = list(larger_poly)
        smaller_poly = list(smaller_poly)
        for i in range(0, len(smaller_poly)) :
            larger_poly[i] += smaller_poly[i]
        self.x = tuple(larger_poly)
        return self
    def scalar_multiply(self, n) :
        y = []
        for i, elem in enumerate(self.x) :
            y.append(elem * n)
        self.x = tuple(y)
        return self
    def multiply(self, P) :
        if type(P) != Poly :
            exit("P argument must be instance of Poly class")
        P = list(P.x)
        x = list(self.x)
        y = [0] * (len(P) * len(x))
        for (a, elem) in enumerate(P) :
            for (b, elem2) in enumerate(x) :
                y[ a+b ] += elem * elem2
        for i in range(len(y)-1, -1, -1) :
            if y[i] == 0 :
                y.pop(i)
            else :
                break
        return tuple(y)
    def power(self, n) :
        mulitpler = self
        for i in range(1, n) :
            multiply_res = self.multiply(mulitpler)
            mulitpler = Poly(multiply_res)
        return mulitpler
    def diff(self) :
        y = list(self.x)
        res = [0] * (len(y)-1)
        for i in range(0, len(y)) :
            if i == 0 :
                res[i]=0
            else :
                res[i-1]= y[i] * i
        self.x = tuple(res)
        return self
    def integrate(self) :
        poly = list(self.x)
        poly.append(0)
        res = [0] * len(poly)
        for i in range(0, len(poly)-1) :
            index = i+1
            res[index] = round(poly[i]/index, 2)
        self.x = tuple(res)
        return self
    def eval(self, n) :
        summation = 0
        for i, elem in enumerate(self.x) :
            summation += elem * n**i
        print(summation)    
    def print(self) :
        eq = ''
        for (i, elem) in enumerate(self.x) :
            if elem == 0 :
                continue
            if i == 0 :
                eq += f'{elem}'
            elif i == 1:
                elem = "{:+}".format(elem)
                eq += f'{elem}x'
            else :
                elem = "{:+}".format(elem)
                eq += f'{elem}x^{i}'
        if eq[0] =='+' :
            eq = eq[1:len(eq)]
        print(eq)    

p = Poly((1,0,-2))
p.print()

q = p.power(2)

p.eval(3)

r = p.add(q)
r.print()

r.diff().print()
p.integrate().print()
