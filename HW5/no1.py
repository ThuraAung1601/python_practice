'''
Write a Python program to iterate the step 4-5 calculation of Newton's number guessing method with 5, 6 and 7 time respectively 
in order to compare the approximation results and report your answers in the three decimal points of accuracy.
'''
n = float(input("Enter a number to find its square root:"))
guess = n/2
for i in range(1,8):
    temp = n/guess
    guess = (guess+temp)/2
    if i == 5 or i == 6 or i == 7:
        print(f"Iteration {i}: {round(guess,3)}")
    else:
        pass
