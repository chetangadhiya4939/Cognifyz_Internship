import random


def guess_number():
    target_no = random.randint(1, 100)

    while True:
        guess = int(input("Enter the random no. in (0,100): "))

        if guess < target_no:
            print(f"Your guessed no {guess} is too low.\n")
        elif guess > target_no:
            print(f"Your guessed no {guess} is too high.\n")
        elif guess == target_no:
            print(f"Hurray! You have guessed the same no. {guess}.\n")
            break
        else:
            print("Oops! You couldn't guess the number.")


guess_number()
