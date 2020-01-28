import random

random_number = random.randint(1,10) # number 1-10
guess = None
#handle user guesses
while guess != random_number:
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

print(random_number)



# BONUS - let player play again if they want!