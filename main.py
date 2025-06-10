import time
import json
import random
import config
from config import CHARACTER, HIKU_POEM_FILE, GREETING_MESSAGE, YEAR, TIMES_USED, GO_AWAY_MESSAGE, VANISH_CHARACTER, DELAY

def choose_random_poem():
    try:
        with open("assets/poems.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            poems = data.get("haiku", [])
            if poems:
                return random.choice(poems)["text"]
            else:
                return "No poems found in the file."
    except FileNotFoundError:
        return "Error: File not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format."

def activate_generator():
    while True:
        key = input("Please press 'h' for me to generate a haiku: ").strip().lower()
        if key == "h":
            while True:
                print("\nHere's your haiku:\n")
                print(choose_random_poem())

                again = input("\nWould you like another haiku? (y/n): ").strip().lower()
                if again == "y":
                    continue
                elif again == "n":
                    go_away()
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")  # This was missing!
        else:
            print("Invalid input. Try again!")

def ask_name():
    name = input("What's your name? ")
    print("Hello " + name + " !")

def interview():
    print("Since you are new to this, we'd like to interview you.")
    reason_for_using_this = input("Why are you using this?\n[Write a poem]\n[Just listen to a poem]\n[Other]\n")
    do_you_know_haiku = input("Do you know what a haiku is?\n[y]es\n[n]o\n")
    how_did_you_find_this = input("Where did you find this?\n[Github]\n[Rudy's Tech Website]\n")

def go_away():
    print(GO_AWAY_MESSAGE)
    def vanish():
        time.sleep(DELAY)
        print(VANISH_CHARACTER)
    vanish()

print("Hi! I'm your haiku poem generator " + CHARACTER)

if TIMES_USED == 1:
    ask_name()

if TIMES_USED == 0:
    ask_name()
    interview()

# If you've used this before, please go to the config.py file and change the TIMES_USED variable to 1.

activate_generator()
