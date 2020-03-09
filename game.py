import random
global time
import sys

sleep = 1
max = 100
dice_val = 6


def intro():
    global name
    name = input("What is your name?")
    welcome(name)

def welcome():
    msg = """
      Rules:
      1. Both players start at 0 
         Take turns rolling the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, move up to the top of the ladder.
      3. If you lands on the head of a snake, you slide down to the bottom of the snake.
      4. The first player to get to 100 is the winner.
      5. Hit enter to roll the dice. """
    print(msg)
    
def diceRoll():
    def get_dice_value():
    time.sleep(sleep)
    dice_value = random.randint(1, dice_val)
    print("Its a " + str(dice_val))
    return dice_val
        
def start():
    welcome_msg()
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    player1_name, player2_name = get_player_names()
    time.sleep(SLEEP_BETWEEN_ACTIONS)

    player1_current_position = 0
    player2_current_position = 0

def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


# driver
intro()          
