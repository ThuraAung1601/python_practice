list1 = [3, 1, 1, 1, 2, 7]
list2 = [4, 1, 1, 2, 2, 5]

def get_the_difference(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    for j in list2:
        if j not in list1:
            result.append(j)
    print(result)

get_the_difference(list1, list2)
