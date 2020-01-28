import random

random_number = random.randint(1,10) # number 1-10
#handle user guesses
while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess) #convert string to integer
#   if they guess correct, tell them they won
#       otherwise tell them if they are too high or too low
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("You won!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            random_number = random.randint(1,10) #numbers 1 - 10
            guess = None
        else:
            print("Thank you for playing!")
            break

# BONUS - let player play again if they want!