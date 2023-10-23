'''
No.3
3.1: Write a Python recursive function perm2(t) which, given a tuple t of numbers, prints out all possible
pairs of distinct numbers in t. Each pair that is printed out may not contain duplicating numbers.

for example,
>> perm2((1, 2, 3))
(1,2) (1,3) (2,1) (2,3) (3,1) (3,2)

3.2: Write a Python recursive function perm3(t) which, given a tuple t of numbers, prints out all possible
pairs of distinct numbers in t. Each triple that is printed out may not contain duplicating numbers.

for example,
>> perm3((1, 2, 3, 4))
(1,2,3)(1,2,4)(1,3,2)(1,3,4)(1,4,2)(1,4,3)
(2,1,3)(2,1,4)(2,3,1)(2,3,4)(2,4,1)(2,4,3)
(3,1,2)(3,1,4)(3,2,1)(3,2,4)(3,4,1)(3,4,2)
(4,1,2)(4,1,3)(4,2,1)(4,2,3)(4,3,1)(4,3,2)

3.3: Write a Python recursive function perm(t, n) which, given a tuple t of numbers and
a number n > 0, prints out all possible n-tuples of numbers in t. Each tuple that is printed out
may not contain duplicating numbers. You may assume that n is no greater than the number of 
elements in t.

perm(t,2) should produce same result as perm2.
perm(t,3) should produce same result as perm3.
'''

def perm2_loop(t):
    result = ""
    for i in range(len(t)):
      for j in range(len(t)):
        if t[i] != t[j]:
            result += f"({t[i]}, {t[j]})"
    return result
# print(perm2_loop((1, 2, 3)))

def perm3_loop(t):
    result = ""
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if t[i] != t[j] and t[j] != t[k] and t[i] != t[k]:
                    result += f"({t[i]}, {t[j]}, {t[k]})"
    return result
# print(perm3_loop((1, 2, 3, 4)))

def perm2(t, i=0, j=0, result=""):
    if i == len(t):
        return result
    if j == len(t):
        return perm2(t, i + 1, 0, result)
    if t[i] != t[j]:
        result += f"({t[i]}, {t[j]})"
    return perm2(t, i, j + 1, result)
# perm2((1, 2, 3))

def perm3(t, i=0, j=0, k=0, result=""):
    if i == len(t):
        return result
    if j == len(t):
        return perm3(t, i + 1, 0, 0, result)
    if k == len(t):
        return perm3(t, i, j + 1, 0, result)
    if i != j and j != k and i != k:
        result += f"({t[i]}, {t[j]}, {t[k]})"
    return perm3(t, i, j, k + 1, result)
# print(perm3((1, 2, 3, 4)))
    
def perm(t, N, current_tuple=(), result=""):
    if N == 0:
        result += f"{current_tuple}"
        return result
    for i in range(len(t)):
        if t[i] not in current_tuple:
            result = perm(t, N - 1, current_tuple + (t[i],), result)
    return result
# print(perm((1, 2, 3, 4), 3))

t = (1, 2, 3)
print("Tuple: f{t}")
print("perm2(t):", perm2(t))
print("perm(t,2):", perm(t,2))
print("perm2(t):", perm3(t))
print("perm(t,3):", perm(t,3))