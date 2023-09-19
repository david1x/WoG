from time import sleep
from vaidate_number import is_it_a_number

def generate_number(difficulty):
    # Will generate automatic random number
    import random
    secret_number = int(random.uniform(1, difficulty))
    print(f"DEBUG: secret_number = {secret_number}")
    return secret_number


def get_guess_from_user(difficulty):
    # The user will choose a number
    # number = int(input(f"You need to guess a number between 1 to {difficulty}: "))
    number = f"You need to guess a number between 1 to {difficulty}: "
    number = is_it_a_number(number)

    return number


def compare_results(secret_number, number):
    # checking if the number the user chose equal to the random number
    if secret_number == number:
        return True


def play(difficulty):
    # The start function, will start all functions and return false or true
    secret_number = generate_number(difficulty)

    print("Generating a Number....")
    sleep(2)
    print("Yeap! The number is ready. Now it is Your turn")
    sleep(1)
    number = get_guess_from_user(difficulty)
    if compare_results(secret_number=secret_number, number=number):
        print("Your guess is correct you WIN!\n")
        return True
    else:
        print("Your guess is incorrect you LOSE!\n")
        return False