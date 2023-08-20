'''
No.6 
Write a function to return an integer 
whose digits are in the reversed orders of the given integer.
For example, reverse(3456) returns 6543
'''

def reverse(num):
    result_str = str(num)[::-1]
    result = int(result_str)
    return result

def main():
    num = int(input("Enter a number:"))
    print(reverse(num))

main()
