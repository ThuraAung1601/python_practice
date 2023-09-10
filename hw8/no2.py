'''
No.2
Write a Python program for reading a string from the user then
printing the frequency distribution of each character occurring
in the string (that is, the percentage of the length of the whole string).
'''
def freq_distro(text):
    freq = {}
    for c in text:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

def main():
    text = input("Enter some text:")
    freq = freq_distro(text)
    # print(freq)
    print("-- Character Frequency Table -")
    for i in freq:
        char_percentage = freq[i] / len(text)
        print("{}{:>10.2%}".format(i, char_percentage))

main()
