'''
No.2
Let f be the function on natural numbers defined recursively as follows:
f(0) = 0
f(n) = 2 * f(n/2) + 1 , if n > 0 and n is even,
f(n) = 0, if n > 0 and n is odd.

Write a function display_f(n) which given an integer n>=0, prints out the value of
f(0), f(1), ..., f(n).
'''

def f(n):
    if n == 0:
        return 0
    elif n > 0 and n%2 == 0:
        return 2*f(n/2) + 1
    else:
        return 0

def display_f(n):
    if n >= 0:
        for i in range(n):
            print(f"{f(i)}", end = ",")
        print(f"{f(n)}")
    else:
        print("Input should be 0 or more.")

# display_f(5)
   
n = int(input("Enter a non-negative integer n: "))
display_f(n)