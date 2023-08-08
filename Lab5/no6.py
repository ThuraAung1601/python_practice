num = eval(input("Enter the num of line: "))

for i in range(1,num//2+1):
    for j in range(i,0,-1):
        print(2**(j-1), end="") 
    print()

if num%2 != 0:
    for i in range(num//2+1,0, -1):
        for j in range(i,0,-1):
            print(2**(j-1), end="") 
        print()
else:
    for i in range(num//2,0, -1):
        for j in range(i,0,-1):
            print(2**(j-1), end="") 
        print()   