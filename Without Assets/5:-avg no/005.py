#Write a Python function that calculates the average of a list of numbers.

def avg(n):
    ab = len(n)
    aa = 0
    for i in range(ab):
        aa += n[i]
    avrage  = aa/ab
    print(n, avrage)

list = [2, 1, 4, 5, 6, 56, 52, 7, 44, 88, 95, 11]
avg(list)
