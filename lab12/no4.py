'''
Author: Kasitphoom Thowongs https://github.com/Kasitphoom
'''
sup = set([1, 2, 3, 4])
sub1 = set([1, 2])
sub2 = set([])
sub3 = set([1, 2, 3, 5])

def is_subset(sup, sub):
    if all(i in sup for i in sub):
        return True
    else:
        return False
    
print(is_subset(sup, sub1))   
print(is_subset(sup, sub2))  
print(is_subset(sup, sub3))    
