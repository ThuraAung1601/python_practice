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
        # if it is duplicated, the value will be more than 1 time
        # try the following in the terminal/ Python shell
        # ls = [1, 2, 1, 3, 4]
        # ls.count(1) # output will be 2 cuz there are two 1s in the list ls
        if name_list.count(value) > 1:
            duplicated[key] = value

    return duplicated

print(find_duplicates(myDict))
