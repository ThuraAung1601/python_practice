# No.3 Greatest Common Divisor
# Using recursion
# def gcd(num1, num2):
#     # print(num1, num2)
#     if num2 == 0:
#         return num1
#     else:
#         return gcd(num2, num1%num2)
# print(gcd(16,310))

# Using ordinary loop
a, b = 16, 310
while b != 0:
    # print(a)
    a, b = b, a%b
print(a)
