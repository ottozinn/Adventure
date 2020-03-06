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

def welcome(name):
    global name
    print("Welcome, " + name)
    print("I will pay you 500 dollars if you beat me in this game")
    print("1. Both players start at 0")
    print("2. If you come to rest at the bottom of a latter, you get to move to the top of it")
    print("3. If you come to rest on the top of a snak, you have to move down to the bottom of it")
    print("4. Hit enter to roll the dice")
def diceRoll():
    min = 1
    max = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        print random.randint(min, max) 
        roll_again = raw_input("Roll the dice again?")
    if int == 1:
        


# driver
intro()          
