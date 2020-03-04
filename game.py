import random
global name

def intro():
    global name
    name = input("What is your name?")
    welcome(name)

def welcome(name):
    global name
    print("Welcome, " + name)
    print("I will pay you 500 dollars if you beat me in this game")

    

def diceRoll():
    min = 1
    max = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print "Rolling the dices..."
        print "The values are...."
        print random.randint(min, max) 
        roll_again = raw_input("Roll the dice again?")
    if int == 1:
        


# driver
intro()          
