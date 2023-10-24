'''
Write a function find_member_positions(number, list_of_numbers) to find all positions where 
number is in the list list_of_numbers. That is, the function returns a list of all positions
of the number in the list; if number is not in the list, the function returns 0.
'''

def find_member_positions(number, list_of_numbers):
    result = []
    if number in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if number == list_of_numbers[i]:
                result.append(i)
            else:
                pass
    else:
        result = 0
    return result

print(find_member_positions(2, [2, 5, 3, 2, 4])) # [0, 3]
print(find_member_positions(1, [2, 5, 3, 2, 4])) # 0