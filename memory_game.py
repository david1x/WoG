import time
import os


def generate_sequence(difficulty):
    # Generate 5 Random numbers, creates a list and prints it
    import random
    random_numbers = []
    for number in range(difficulty):
        random_numbers.append(int(random.uniform(1, 101)))
    print(random_numbers)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    return random_numbers


def get_list_from_user(difficulty):
    # The user choose 5 numbers
    user_numbers = []
    print(f"Please Insert {difficulty} numbers")
    for i in range(difficulty):
        i = user_numbers.append(int(input("Import a Number: ")))
    return user_numbers


def is_list_equal(random_numbers, user_numbers):
    # Checking if the lists are equal
    random_numbers.sort()
    user_numbers.sort()
    os.system('cls' if os.name == 'nt' else 'clear')
    if random_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    # The start function, will start all functions and return false or true
    random_numbers = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)
    if is_list_equal(user_numbers=user_numbers, random_numbers=random_numbers):
        print("Your Memory is Impeccable!")
        return True
    else:
        print("You guessed incorrectly...Good luck next time!")
        return False