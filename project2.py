import random as r

print("-----WELCOME TO THE ULTIMATE GUESS GAME-----")

n = r.randint(1,50)
print("Can you guess the number in as least tries as possible?\n")
choice = int(input("Guess the number: "))

tries = 1
while (choice != n):
    if (choice > n):
        print("\nThe number is lower than your guess.\n")
        tries+=1
    
    elif (choice < n):
        print("\nThe number is higher than your guess.\n")
        tries+=1
        
    choice = int(input("Guess the number: "))

if (choice == n):
    print("\nBingo! You guessed it.")

print(f"It took you {tries} tries.\n")
