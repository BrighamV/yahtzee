"""
Yahtzee!!!

Created by: Brigham Valentine

"""
import random

def start():
    print("Would you like to play Yatzee?")
    choice = input("Start New Game? y/n: ")
    if choice == "y" or choice == "Y":
        print()
        display()
    elif choice == "n" or choice == "N":
        return 0
    else:
        start()
        
def display():
    print("What would you like to do with your dice?")
    print("Roll: r")
    print("Quit Game: q")
    choice = input(">: ")
    print()
    if choice == "r" or choice == "R":
        roll()
    elif choice == "q" or choice == "Q":
        return 0
    else:
        display()
    

        
def displayDice(dice):
    if dice == 1:
        print("#######")
        print("#     #")
        print("#     #")
        print("#  *  #")
        print("#     #")
        print("#     #")
        print("#######")
    elif dice == 2:
        print("#######")
        print("# *   #")
        print("#     #")
        print("#     #")
        print("#     #")
        print("#   * #")
        print("#######")
    elif dice == 3:
        print("#######")
        print("# *   #")
        print("#     #")
        print("#  *  #")
        print("#     #")
        print("#   * #")
        print("#######")
    elif dice == 4:
        print("#######")
        print("# * * #")
        print("#     #")
        print("#     #")
        print("#     #")
        print("# * * #")
        print("#######")
    elif dice == 5:
        print("#######")
        print("# * * #")
        print("#     #")
        print("#  *  #")
        print("#     #")
        print("# * * #")
        print("#######")
    else:
        print("#######")
        print("# * * #")
        print("#     #")
        print("# * * #")
        print("#     #")
        print("# * * #")
        print("#######")
    print()
    
def roll():
    num = int(input("How many dice would you like to roll?: "))
    
    
    while num > 0:
      
        dice = random.randrange(1, 6)
        displayDice(dice)
        num = num -1
     
    display()
         
         


start()
