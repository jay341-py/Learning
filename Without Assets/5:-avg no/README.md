# Average Calculator (Manual Method)

This Python script defines a function to calculate the average of a list of numbers using a basic loop—without relying on built-in functions like sum() or statistics.mean().
## 🧠 Purpose

To help beginners understand how averages are calculated step by step through loops and counters.
## 📝 Function Definition

def avg(n):
    ab = len(n)
    aa = 0
    for i in range(ab):
        aa += n[i]
    avrage = aa / ab
    print(n, avrage)

## 🚀 How It Works

    Takes a list n as input.

    Calculates the total number of elements using len(n).

    Initializes a sum counter aa and loops through the list to sum all values.

    Divides the total sum by the number of elements to get the average.

    Prints the original list and the calculated average.

## 💡 Example Usage

list = [2, 1, 4, 5, 6, 56, 52, 7, 44, 88, 95, 11]
avg(list)

Output:

[2, 1, 4, 5, 6, 56, 52, 7, 44, 88, 95, 11] 30.75

## ❌ Limitations

    Uses print() inside the function. In real applications, it's better to return the value.

    Variable name list should be avoided because it overrides the built-in list type in Python.

    Typo in avrage variable name (should be average for clarity).
