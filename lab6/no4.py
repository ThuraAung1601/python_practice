def sum_of_digit(num):
    sum = 0
    num_lst = list(num)
    for i in range(0, len(num_lst)):
        sum += int(num_lst[i]) 
    return sum

def main():
    num = input("Enter the number: ")
    result = sum_of_digit(num)
    print(f"The sum is {result}")

main()