num = int(input("Input: "))
if num >= 1:
    for k in range(num, 0, -1):
        for i in range(1,k):
            for j in range(0,i):
                print("*",end="")
            print()
        if k <= 2:
                for i in range(k,0,-1):
                    for j in range(i,0,-1):
                        print("*",end="")
                    print() 
        else:        
            for i in range(k,1,-1):
                for j in range(i,0,-1):
                    print("*",end="")
                print() 
else:
    print("Invalid input. Input must be greater than or equal to 1.")
    quit()

# Recursive version
# def pattern_generator(num):
#     if num >= 0:
#         for i in range(1,num):
#             for j in range(0,i):
#                 print("*",end="")
#             print()
#         if num <= 2:
#             for i in range(num,0,-1):
#                 for j in range(i,0,-1):
#                     print("*",end="")
#                 print() 
#         else:        
#             for i in range(num,1,-1):
#                 for j in range(i,0,-1):
#                     print("*",end="")
#                 print() 
#         pattern_generator(num-1)

# num = int(input("Input: "))
# if num >= 1:
#     pattern_generator(num)
# else:
#     print("Invalid input. Input must be greater than or equal to 1.")
#     quit()
