import random


# validate user input
def validate_in_range(user_input):
    if user_input > 10:
        print("Please enter a number less than ten")


def main():
    # simple python guessing number game
    user_number = int(input("Can you guess the number between 1 to 10? "))
    user_tries = 1
    python_guessed = random.randint(1, 10)

    while user_tries != 3:
        if user_number != python_guessed:
            user_tries += 1
            user_number = int(input("Try again please: "))
        else:
            print("You guessed the right number", python_guessed, sep="")

    print("Sorry you've run out of tries, the number is:", python_guessed)

main()
