list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
def remove_the_thirds(list1):
    for i in range(len(list1)):
        # print(i, list1[i])
        if (i+1)%3 == 0:
            # print(list1[i])
            list1[i] = ''
    while '' in list1:
        list1.remove('')
    print(list1)
remove_the_thirds(list1)