'''
No. 3
Write Python three functions which, given any two lists, 
returns a list which represents a union, an intersection,
and a difference of the two lists, respectively.
'''
list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

def my_union(list1, list2):
    result = []
    for i in list1:
        result.append(i)
    for j in list2:
        if j in list1:
            continue
        else:
            result.append(j)
    return result

def my_intersection(list1, list2):
    # [x for x in list1 if x in list2]
    result = []
    for i in list1: 
        if i in list2:
            result.append(i)
    return result

def my_difference(list1, list2):
    # [x for x in list1 if x not in list2]
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))