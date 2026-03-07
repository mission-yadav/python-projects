# Rock, Paper, Scissors Game
# Player VS Computer
"""

1 for rock
0 for paper
-1 for scissors

"""
import random

computer=random.choice([1,0,-1])
player=(input("Enter your choice: "))
playerdict={ "r" : 1, "p": 0, "s" : -1 }
revdict={ 1 : "Rock", 0 : "Paper", -1 : "Scissors" }
you= playerdict.get(player)
print(f"You chose {revdict[you]}\nComputer chose {revdict[computer]}..... ")

if(computer == you):
    print("It is a Draw !")

else:
    if(computer == 1 and you == 0):
        print("You Win !")

    elif(computer == 1 and you == -1):
        print("You Lose !")

    elif(computer == 0 and you == 1):
        print("You Lose !")

    elif(computer == 0 and you == -1):
        print("You Win !")

    elif(computer == -1 and you == 1):
        print("You Win !")

    elif(computer == -1 and you == 0):
        print("You Lose !")

    else:
        print("INVALID !")


