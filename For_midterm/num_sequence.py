for i in range(50, 0, -1):
    if i%3 == 0 or i%5 == 0: continue
    elif i != 1: print(i, end=",")
    else: print(i, end=".\n")

# result = ""
# for i in range(50, 0, -1):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     result += f"{i}, " if i != 1 else f"{i}.\n"

# print(result)
