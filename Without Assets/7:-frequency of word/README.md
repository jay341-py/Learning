# Character Frequency Counter

This Python script defines a simple function that counts how many times each character appears in a given string, without using any built-in functions like collections.Counter.
## 🧠 Purpose

To help beginners understand how dictionaries can be used to store and update the frequency of items (in this case, characters).
## 📝 Function Definition

def feq(aa):
    ab = {}
    for i in aa:
        if i in ab:
            ab[i] += 1
        else:
            ab[i] = 1
    return ab

    aa: Input string.

    ab: Dictionary to store frequencies.

    Iterates through each character and counts its occurrences.

## 💡 Example Usage

print(feq("jayendra"))

Output:

{'j': 1, 'a': 2, 'y': 1, 'e': 1, 'n': 1, 'd': 1, 'r': 1}

## 📌 How It Works

    Initializes an empty dictionary ab.

    Loops through each character in the input string aa.

    If the character already exists in ab, increments its count.

    If it doesn’t exist, sets its count to 1.

    Returns the dictionary with frequencies.
