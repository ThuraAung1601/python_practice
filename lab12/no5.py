s = set([1, 2, 3])

def power(s):
    if len(s) == 0:
        return {frozenset()}
    else:
        x = s.pop()
        p = power(s)
        return p.union({e.union({x}) for e in p})

print(power(s))

        

    