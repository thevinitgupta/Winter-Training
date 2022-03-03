#guessing game -> between 1-100 after how many attempts
import random
rand = random.randrange(1,100)

guessed = False
attempts = 0
while not guessed :
    val=int(input("Guess a number"))
    attempts += 1
    if val==rand :
        print("Guessed in",attempts,"attempts!")
        guessed = True
    elif val<rand :
        print("Guess higher")
    else :
        print("Guess lower")
