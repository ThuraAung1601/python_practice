'''
No.2: Given two dictionaries dict1 and dict2, suppose we define the composition of dict1 and dict2 
to be the dictionary dict3 such that a (key: value) - pair k:v is in dict3, if and only if there exists
some object m such that k:m is in dict1 and m:v is in dict2.
Write a Python function composite(dict1, dict2) which returns the composite of the given dictionaries dict1
and dict2.
'''
dict1 = {
    'a': 'p',
    'b': 'r',
    'c': 'q',
    'd': 'p',
    'e': 's'
}

dict2 = {
    'p': '1',
    'q': '2',
    'r': '3'
}

def composite(dict1, dict2):
    dict3 = {}
    for k, m1 in dict1.items():
        for m2, v in dict2.items():
            if m1 == m2 and k not in dict3:
                dict3[k] = v
            else:
                pass
    return dict3

print(composite(dict1, dict2))