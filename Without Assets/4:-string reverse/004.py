#Write a Python function that reverses a given string without using built-in reverse functions.

def sting(aa):
    ab = ''
    for i in aa:
        ab = i + ab
    print(ab)
    return ab


sting("jayendra")
