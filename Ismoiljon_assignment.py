# Student: Abduraimov Ismoiljon Odiljon Ugli
# Student ID: 202380107

import random

rand_number = random.randint(0, 100)


def guess_check(rand_number, guess):
    if guess == rand_number:
        return 0
    elif guess < rand_number:
        return -1
    else:
        return 1


attempts = 0
while True:
    guess = int(input("Guess the number between 0 and 100: "))

    result = guess_check(rand_number, guess)

    if result == 0:
        print(
            f"Congratulations! You've guessed the number {rand_number} correctly in {attempts} attempts.")
        break
    else:
        if result == -1:
            print("The number is higher. Try again.")
        else:
            print("The number is lower. Try again.")
        attempts += 1
