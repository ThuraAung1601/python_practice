def reverse(num):
    result_str = num[::-1]
    result = int(result_str)
    return result

def main():
    num = input("Enter a number:")
    print(reverse(num))