#Write a Python function that counts the frequency of each character in a string.

def feq(aa):
    ab = {}
    for i in aa:
        if i in ab:
            ab[i] += 1
        else:
            ab[i] = 1
    return ab

print(feq("jayendra"))
