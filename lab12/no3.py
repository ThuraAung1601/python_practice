dict = {
    'a': '1',
    'b': '2',
    'c': '1',
    'd': '3',
    'e': '1',
    'f': '2',
}

def inverse(dict):
    inverse = {}
    for key, value in dict.items():
        if value not in inverse:
            inverse[value] = set([key])
        else:
            inverse[value].add(key)
    return inverse

print(inverse(dict))
