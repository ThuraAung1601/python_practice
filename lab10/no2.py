# # No.2 Inverse of a list
# # Using recursion
# def inverser(l):
#     if len(l) == 0:
#         return []
#     else:
#         return inverser(l[1:]) + [l[0]]
# print(inverser([1, 2, 3, 4, 5, 6]))

# Using ordinary loop
l = [1, 2, 3, 4, 5, 6]
reverse = []
for i in range(len(l)-1, -1, -1):
    reverse += [l[i]]
print(reverse)
