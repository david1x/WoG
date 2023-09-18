import random
import os
import requests



def get_money_interval(difficulty):
    # Will get the Current currency
    # and generate an int : difficulty = d, money = t [(t - (5 - d), t + (5 - d))]
    # API key from "free.currencyconverterapi.com": 2e015e19466c486dc19f
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=0163128afebbf1c47d33"
    response = requests.get(url, verify=False)
    data = response.json()
    # ex: exchange rate USD ILS
    # usd: Random numbers of USD
    # t: The Value of ILS in USD currency
    ex = int(data["USD_ILS"])
    usd = int(random.uniform(1, 100))
    result = usd * ex
    low = int(result - (10 - difficulty))
    high = int(result + (10 - difficulty))
    return usd, result, low, high


def get_guess_from_user(usd):
    # User needs to guess the Value to a given amount of USD
    while True:
        try:
            guess = int(input(f"Guess the value of {usd}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        return guess


def play(difficulty):
    # Will call all other functions to start the game
    usd, result, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(usd)
    os.system('cls' if os.name == 'nt' else 'clear')
    if high >= guess >= low:
        print("Your guess is correct you WIN!")
        return True
    else:
        print("Your guess is incorrect you LOSE!")
        return False

