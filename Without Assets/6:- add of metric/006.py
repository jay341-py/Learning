#Write a Python function that adds two matrices.
import random as rd

def list(n,a,b):
    l=[]
    for i in range(n):
        r=rd.randint(a,b)
        l.append(r)
    if len(l) != n:
        list(n, a, b)
    return l


def matrices():
    ma = []
    for i in range(3):
        ma.append(list(3, 1, 10))
    print(ma)
    return ma


def add_matrices():
    aa = matrices()
    ab = matrices()
    aaa = len(aa)
    aba = len(ab)
    ac = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ad = []
    for i in range(aaa):
        for j in range(len(aa[i])):
            ac[i][j] = aa[i][j] + ab[i][j]
    return ac


print(add_matrices())
