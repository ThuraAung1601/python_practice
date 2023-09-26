list1 = [111, 61, 16, 5]
list2 = [2, 4, 11, 5, 6]

def sort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp
            else:
                pass
    return ls


print(sort(list1))
print(sort(list2))

def merge(list1, list2):
    result = list1 + list2
    return sort(result)

print(merge(list1, list2))

a = [1, 3, 5 ,7 ,9]
b = [2, 4, 6, 8, 10]
c = merge(a, b)
print("base list")
print(a)
print(b)
print("answer list")
print(c)


d = [1, 1, 1, 1, 8, 8, 8, 8, 8, 15, 15, 15, 15]
e = merge(d, b)
print("base list")
print(d)
print(b)
print("answer list")
print(e)

