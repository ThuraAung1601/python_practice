n = float(input("Enter a number to find its square root:"))
guess = n/2
for i in range(1,8):
    temp = n/guess
    guess = (guess+temp)/2
    if i == 5 or i == 6 or i == 7:
        print(f"Iteration {i}: {round(guess,3)}")
    else:
        pass