myDict = {
    's5301': 'Fred',
    's5302': 'Harry',
    's5303': 'John',
    's5304': 'Fred',
    's5305': 'Harry'
}

def find_duplicates(dict):
    duplicated = {}
    name_list = list(dict.values())

    for key, value in dict.items():
        if name_list.count(value) > 1:
            duplicated[key] = value

    return duplicated

print(find_duplicates(myDict))