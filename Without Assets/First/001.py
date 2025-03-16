# Write a Python program that generates a random number between 1 and 100 and asks the user to guess it,
# providing feedback on whether the guess is too high or too low.
import random as rd


def no():
    r = rd.randint(1, 100)
    return r


def gas():
    print("Guess the number between 1 to 100")
    aa = int(input())
    return aa


def main(ab, ar):
    found = True
    while found:
        try:
            if ab > ar+10:
                print("Its too high")
            elif ab > ar:
                print("Its high")
            elif ab < ar-10:
                print("Its too low")
            elif ab < ar:
                print("Its low")
            elif ab == ar:
                print("You have guess right")
                found = False
                break
            print("Guess it again")
            ab = int(input())
        except ValueError:
            print("invalid literal for int() with base 10")


main(gas(), no())
