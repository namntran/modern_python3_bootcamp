import random
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make  your move: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"   
else: 
     computer = "scissors"
print(f"computer plays {computer}")

# player2 = input("Player 2, make  your move: ")

if player == computer:
    print("it's a tie")

elif player == "rock":
    if computer == "scissors":
        print("player wins")
    elif computer == "paper":
        print("computer wins")
    else:
        print("something went wrong")

elif player == "paper":
    if computer == "scissors":
        print("computer wins")
    elif player == "rock":
        print("player wins")
    else:
        print("something went wrong")

elif player == "scissors":
    if computer == "rock":
        print("computer wins")
    elif computer == "paper":
        print("player wins")
    else:
        print("something went wrong")