'''
Given a dictionary popularity_scores taken from an IEEE spectrum ranking, define a Python
function to process this dictionary and return a dictionary that represents the computer language
ranking on the right based on the popularity scores of the computer languages on the left.
'''

popularity_scores = {
    "C++": 99.7,
    "C": 96.7,
    "Java": 97.5,
    "Rust": 97.5,
    "Python": 100,
    "C#": 86.1
}

def ranking(popularity_scores):
    # convert the dictionary data to list to sort
    temp = []
    for langauge, score in popularity_scores.items():
        temp.append([langauge, score])
    # sorting by applying bubble sort
    for i in range(len(temp)):
        for j in range(len(temp)-i-1):
            if temp[j][1] < temp[j+1][1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            elif temp[j][1] == temp[j+1][1]:
                temp[j][0] += ", " + temp[j+1][0]
                del temp[j+1]
            else:
                pass

    print(temp)
    # making dictionary
    ranked = {}
    for i in range(len(temp)):
        if i+1 not in ranked:
            ranked[i+1] = temp[i][0]
        else:
            pass
    return ranked

print(ranking(popularity_scores))
# {1: 'Python', 2: 'C++', 3: 'Java', 4: 'C', 5: 'C#'}
