'''
A single-variable polynomial can be represented in Python as a tuple of coefficient.
For example, the polynomial 14+7x-5x^2+18x^5 can be represented as (14, 7, -5, 0, 0, 18).
'''
class Poly:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def print(self):
        power = len(self.coefficients) - 1
        poly_str = ""

        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                if i == 0:
                    poly_str += str(coeff)
                else:
                    if coeff > 0:
                        poly_str += " + "
                    else:
                        poly_str += " - "
                    if abs(coeff) != 1 or i == power:
                        poly_str += str(abs(coeff)) + "x" + "^" + str(power)
                    if i < power:
                        poly_str += "x"
                    if i < power - 1:
                        poly_str += "^" + str(power - i)
        print(poly_str)

    def eval(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** (len(self.coefficients) - 1 - i))
        print(result)

p = Poly((1, 0, -4, 0, 4))
p.print()
p.eval(3)