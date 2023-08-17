num = input("Enter a number:")
def rev_int(num):
    num_list = [c for c in num]
    rev_num_list = num_list[::-1]
    result_str = "".join(rev_num_list)
    result = int(result_str)
    return result
print(rev_int(num))