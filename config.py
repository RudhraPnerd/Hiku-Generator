CHARACTER = "^*^" #You can pick from a wide range of kaomojis to choose from in the haiku_characters.txt file which is
                  #stored in assets/characters/haiku_characters.txt
VANISH_CHARACTER = "👻" #There's only a small list of emojis you can choose but if you still want to use one of them, go
                        #to assets/characters/vanish_character.txt
SCREEN_TYPE = "Console"
HIKU_POEM_FILE = "assets/poems.json"
GREETING_MESSAGE = "Welcome to the Hiku Generator"
GO_AWAY_MESSAGE = "OK, hope you liked the haiku's, goodbye!"
YEAR = 2025
TIMES_USED = 1
DELAY = 1.5


#If attempting to run this

import sys


def empty():
    empty_message = "Nothing to show"
    print(empty_message)

def do_nothing():
    pass

code = 0

if code == 0:
    empty()
    sys.exit()

if code == 1:
    do_nothing()



