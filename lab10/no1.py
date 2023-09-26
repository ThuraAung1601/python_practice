# No.1 Check list member or not
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

# Using ordinary loop
l = [1, 2, 4, 5, 6]
e = 9
for i in range(len(l)):
    if e == l[i]:
        print(True)
        break
    else:
        continue
print(False)
