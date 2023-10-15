'''
No.1: To save time and spcae when sending an SMS or a tweet, some words or phrases are often abbreviated.
Below is a list of commonly-used abbreviations.
1.1: Write a function textese(s) which, given a string s of message in plain English, returns a string 
resulted from replacing words or phrases in s using the above abbreviations. The abbreviated string
should be as short as possible.
1.2: Write function untextese(s) which, given a string s of message employing the above abbreviations, 
returns a string of message in plain English.
'''

abbrev = {
    "be": "b",
    "because": "cuz",
    "see you": "cu",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    'before': "b4",
    "once": "1ce",
    "and": "&",
    "your": "ur",
    "you're": "ur",
    "as far as I know": "afaik",
    "as soon as possible": "asap",
    "at the moment": "atm",
    "be right back": "brb",
    "by the way": "btw",
    "for your information": "fyi",
    "in my humble opinion": "imho",
    "in my opinion": "imo",
    "laugh out loud": "lol",
    "oh my god": "omg",
    "roll on the floor laughing": "rofl",
    "talk to you later": "ttyl"
}

def textese(s):
    s = s.lower()
    for i in abbrev:
        if i in s:
            s = s.replace(i, abbrev[i])
    return s

s1 = "Oh my god Let me be your friend as soon as possible"
print(textese(s1))

def untextese(s):
    unabbrev = {}
    for key, value in abbrev.items():
        if value not in unabbrev:
            unabbrev[value] = key
        else:
            pass
    s = s.lower()
    ls = s.split()
    for i in ls:
        if i in unabbrev:
            s = s.replace(i, unabbrev[i])
    return s

s2 = "ur father ask me to cu ASAP m8"
print(untextese(s2))
