def name_list():
    result = []
    i = 1
    while True:
        name = input(f"Enter ur name {i}: ")
        i += 1
        if name == "": break
        else: result.append(name)
    print(result)

name_list()