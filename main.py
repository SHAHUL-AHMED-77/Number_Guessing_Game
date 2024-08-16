import random
import math
def Number_Guessing_game():
    lower = int(input("Enter Lower Bound Number :"))
    upper = int(input("Enter Upper Bound Number :"))

    choice = random.randint(lower, upper)

    chances = math.ceil(math.log(upper - lower+1,2))


    print(f"You have {chances} To Guess The Number")


    count = 0

    while count < chances:
        guess = int(input("Guess the Number : "))
        count += 1
        if guess == choice:
            print(f"Congratulations!!! You Guessed It Correctly in {count} tries")
            break
        elif guess < choice:
            print("Too Low, Try Again!")
        else:
            print("Too High, Try Again!")

Number_Guessing_game()