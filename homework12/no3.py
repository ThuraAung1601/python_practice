'''
No.3: Suppose we are given sets s and t. The Cartesian product of s and t is the set of all 
tuples (x,y) such that x is a member of s and y is a member of t.
More generally, suppose we are given N sets, s1, ..., sN (where N>=1). The Cartesian product of
s1, ..., sN is the set of all N-tuples (x1, ..., xN) such that x1 is a member of s1, ..., and
xN is a member of sN.
Write a Python funciton product(s1, ..., sN), where s1, ..., sN are the sets and N>=1, which 
returns the Cartesian product of s1, ..., sN.
'''
s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

def product(*sets):
    if not sets:
        return [()]
    result = [[]]
    for s in sets:
        result = [x + [y] for x in result for y in s]
    return set([tuple(item) for item in result])

result1 = product(s1)
print(result1)

result2 = product(s1, s2)
print(result2)

result3 = product(s1, s2, s3)
print(result3)