sum = 0

for i in range(0,5):
    num = int(input("Enter an integer: "))
    if num < 0:
        if sum < 0:
            sum += num
        else:
            sum = 0
            sum += num
    elif num > 0:
        if sum > 0:
            sum += num
        else:
            sum = 0
            sum += num
    else:     
        sum += num

    print("Current sum:",sum)
