import random
import time
import sys

sleep = 1
max = 100
dice_val = 6

snakes = {
    7: 1,
    29: 13,
    49: 23,
    63: 32,
    77: 30,
    99: 5
}

ladders = {
    8: 69,
    19: 31,
    44: 52,
    55: 61,
    72: 98,
    83: 91,
}


def welcome():
    msg = """
      Rules:
      1. Both players start at 0 
         Take turns rolling the dice. 
         You automatically move forward the number of spaces shown on the dice
      2. If you lands at the bottom of a ladder, move up to the top of the ladder
      3. If you lands on the head of a snake, you slide down to the bottom of the snake
      4. The first player to get to 100 wins.
      5. Denton will always lose
      6. Hit enter to roll the dice """
    print(msg)
    
def diceRoll():
    time.sleep(sleep)
    dice_value = random.randint(1, dice_val)
    print("Its a " + str(dice_val))
    return dice_val
        
def start():
    time.sleep(sleep)
    player1_name, player2_name = get_player_names()
    time.sleep(sleep)

    player1_current_position = 0
    player2_current_position = 0

def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

def snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite :////. You have to move from " + str(old_value) + " to " + str(current_value))


def ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " Climb the ladder :0  " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(sleep)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


# driver
welcome()
diceRoll()
start()

          
