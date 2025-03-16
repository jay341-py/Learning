#Write a Python function that checks if a given string is a palindrome (reads the same forwards and backwards).
import string as st


def pal(word):
    aw = len(word)
    aa = ""
    for i in word:
        aa = i + aa
    return aa == word


wo = 'jayaj'
print(pal(wo))
