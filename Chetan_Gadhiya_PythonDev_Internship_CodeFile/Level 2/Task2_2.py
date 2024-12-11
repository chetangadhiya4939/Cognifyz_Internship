import random


def guess_number():
    lower_bound = int(input("Enter lower bound : "))
    upper_bound = int(input("Enter upper bound : "))

    if lower_bound >= upper_bound:
        print("lower bound must be lesser than upper bound.")
        return
    target_no = random.randint(lower_bound, upper_bound)

    while True:
        guess = int(input(f"Enter the random no. in ({lower_bound},{upper_bound}): "))

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
