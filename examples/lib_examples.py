import random

# generates a random number from 0.0 - 1.0
random_num = random.random()
print(random_num)

# generates a random number from given choices
random_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(random_choice)

# generates a random int in given range
random_range = random.randint(1, 100)
print(random_range)
