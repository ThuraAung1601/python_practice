# # No.1 Check list member or not
# # Using recursion
# def chk_list_member(l, e):
#     if len(l) == 0:
#         return False
#     else:
#         if e == l[0]:
#             return True
#         else:
#             return chk_list_member(l[1:], e)
# print(chk_list_member([1, 2, 4, 5, 6], 6))
# print(chk_list_member([1, 2, 4, 5, 6], 7))

# # Using ordinary loop
# l = [1, 2, 4, 5, 6]
# e = 9
# for i in range(len(l)):
#     if e == l[i]:
#         print(True)
#         break
#     else:
#         continue
# print(False)

# # No.2 Inverse of a list
# # Using recursion
# def inverser(l):
#     if len(l) == 0:
#         return []
#     else:
#         return inverser(l[1:]) + [l[0]]
# print(inverser([1, 2, 3, 4, 5, 6]))

# # Using ordinary loop
# l = [1, 2, 3, 4, 5, 6]
# reverse = []
# for i in range(len(l)-1, -1, -1):
#     reverse += [l[i]]
# print(reverse)

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
# a, b = 16, 310
# while b != 0:
#     # print(a)
#     a, b = b, a%b
# print(a)

# # No.4
# import turtle
# import random

# turtle.speed(0)
# turtle.Turtle()

# def cross(width, times):
#     if times == 0:
#         hexadecimal = "#" + ''.join([random.choice("ABCDEF0123456789") for i in range(6)])
#         turtle.dot(3, hexadecimal)
#         return 
#     else:
#         for i in range(4):
#             turtle.forward(width)
#             cross(width/2, times-1)
#             turtle.right(180)
#             turtle.forward(width)
#             turtle.left(90)

# cross(100, 4)
# turtle.update()
# turtle.done()

# No.5 
# Find the subset of a list which sum is zero
# def subsetSumZero(ls, result = [], Sum = 0):
#     if ls == []:
#         print(result)
#         return [x for x in [result] if sum(x) == 0 and x != []]
#     else:
#         return subsetSumZero(ls[1:], result + [ls[0]], Sum + ls[0]) + subsetSumZero(ls[1:], result, Sum)
        
# subsetSumZero([-7, -3, -2, 5, 7])

# print(subsetSumZero([-7, -3, -2, 5, 7])) 
# [[-7, -3, -2, 5, 7], [-7, 7], [-3, -2, 5]]
# print(subsetSumZero([2, -3, 5, 8 ,11, 23, -1]))
