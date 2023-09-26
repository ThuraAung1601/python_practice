# No.5 
# Find the subset of a list which sum is zero
def subsetSumZero(ls, result = [], Sum = 0):
    if ls == []:
        print(result)
        return [x for x in [result] if sum(x) == 0 and x != []]
    else:
        return subsetSumZero(ls[1:], result + [ls[0]], Sum + ls[0]) + subsetSumZero(ls[1:], result, Sum)
        
subsetSumZero([-7, -3, -2, 5, 7])
