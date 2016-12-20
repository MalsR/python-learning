import random


# validate user input
def validate_in_range(user_input):
    if user_input > 10:
        print("Please enter a number less than ten")
    return


def parse_user_input(user_input):
    try:
        return int(user_input)
    except ValueError as error:
        print("Please enter a number, you've entered ", error)


def main():
    # simple python guessing number game
    user_input = input("Can you guess the number between 1 to 10 (you have 3 tries)? 'Q' to quit! ")
    user_tries = 1
    python_guessed = random.randint(1, 10)

    while user_input.upper() != 'Q':
        if user_tries == 3:
            break

        user_input = parse_user_input(user_input)
        # update logic to not count the turn on validation failure
        validate_in_range(user_input)
        if user_input != python_guessed:
            user_tries += 1
            user_input = input("Try again please: ")
        else:
            print("You guessed the right number", python_guessed, sep="")

    # when number guessed then issue here
    if user_input.upper() == 'Q':
        print("You've quit! :-(")
    else:
        print("Sorry you've run out of tries, the number is:", python_guessed)

main()
