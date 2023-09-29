'''
No. 5
Write a function isAnagram(String1, String2) that decides whether two words (strings)
are anagrams. Some two words are anagrams if they contain the same letters regardless of
the letters' positions.
'''
str1 = "silent"
str2 = "listen"

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] not in str2:
            return False
        else:
            str2.replace(str1[i], "")
    return True
        
print(isAnagram(str1, str2))