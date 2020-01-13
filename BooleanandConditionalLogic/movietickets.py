age = int(input("what is your age?"))

if age > 2 and age < 13:
    print("You are eligible for child price")

elif age <= 2:
    print("You have complimentary ticket")

else:
    print("You must pay the adult price")
