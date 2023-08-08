num = 5

print("Pattern A")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end="") 
    print()

print("Pattern B")
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j, end="") 
    print()

