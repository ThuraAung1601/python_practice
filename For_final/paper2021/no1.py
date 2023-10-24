'''
Write a function find_word_positions(word, list_of_words) to find all positions where 
word is in the list list_of_words. That is, the function returns a list of all positions
of the word in the list; if word is not in the list, the function returns 0.
'''

def find_word_position(word, list_of_words):
    word = word.lower()
    list_of_words = [w.lower() for w in list_of_words]
    result = []
    if word in list_of_words:
        for i in range(len(list_of_words)):
            if word == list_of_words[i]:
                result.append(i)
            else:
                pass
    else:
        result = 0
    return result

print(find_word_position("Hello", ["hello", "world", "hEllO"]))