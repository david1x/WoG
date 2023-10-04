import guess_game
import memory_game
import currency_roulette_game
import os
from score import add_score
global difficultly, choice


def welcome():
    username = input('What is your Name? \n')
    print("-" * 80)
    return f'\nHi {username.title()} and welcome to the World of Games: The Epic Journey \n'


def start_play():
    while True:
        choice = input('''Please choose a game to play:
                        \t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                        \t2. Guess Game - guess a number and see if you chose like the computer
                        \t3. Currency Roulette - try and guess the value of a random amount of USD in ILs\n''')
        if not choice or not choice.isdigit() or int(choice) < 1 or int(choice) > 3:
            print(f'\nInvalid option! Please try again...\n')
        else:
            break

    while True:
        difficultly = input('Please choose game difficultly from 1 to 5:\n')
        if not difficultly or not difficultly.isdigit() or int(difficultly) < 1 or int(difficultly) > 5:
            print(f'\nInvalid option! Please try again...\n')
            continue
        difficultly = int(difficultly)
        if int(choice) == 1:
            # Calling Game number Two (Memory game)
            memory_game.play(difficultly)
            if bool(memory_game) is True:
                add_score(difficultly=difficultly)
        if int(choice) == 2:
            # Calling Game number one (Guess game)
            guess_game.play(difficultly)
            if bool(guess_game) is True:
                add_score(difficultly=difficultly)
        if int(choice) == 3:
            # Calling Game number Two (CurrencyRoulette Game)
            currency_roulette_game.play(difficultly)
            if bool(currency_roulette_game) is True:
                add_score(difficultly=difficultly)
        play_again()

def play_again():
    retry = input("Do you want to play again?\n").title()
    if retry == "Yes" or retry == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        welcome()
        start_play()
    elif retry == "No" or retry == "N":
        exit(0)
    else:
        print("Please type Yes or No. \n")
        play_again()