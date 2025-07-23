# Matrix Addition (3x3 Random Matrices)

This Python script demonstrates how to generate two 3x3 matrices with random integers and add them element-wise without using NumPy or other external libraries.
## 🧠 Purpose

To help understand:

    How to create random matrices manually.

    How to add two matrices element-by-element using loops.

## 📜 Script Overview
Random List Generator

import random as rd

def list(n, a, b):
    l = []
    for i in range(n):
        r = rd.randint(a, b)
        l.append(r)
    if len(l) != n:
        list(n, a, b)
    return l

    Generates a list of n random integers between a and b.

    (Note: The check if len(l) != n: is unnecessary; the loop ensures length.)

## Matrix Generator

def matrices():
    ma = []
    for i in range(3):
        ma.append(list(3, 1, 10))
    print(ma)
    return ma

    Creates a 3x3 matrix with random values between 1 and 10.

## Matrix Addition

def add_matrices():
    aa = matrices()
    ab = matrices()
    ac = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(aa)):
        for j in range(len(aa[i])):
            ac[i][j] = aa[i][j] + ab[i][j]
    return ac

print(add_matrices())

    Fetches two random 3x3 matrices.

    Adds each corresponding element and stores it in a third matrix.

    Prints the result.

## 💡 Sample Output

Each run generates different values. Example:

[[4, 2, 9], [1, 8, 3], [10, 7, 6]]
[[3, 5, 1], [7, 2, 4], [6, 1, 8]]
[[7, 7, 10], [8, 10, 7], [16, 8, 14]]

