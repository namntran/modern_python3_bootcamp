# ask for age
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 18 and age < 21:
        # 18 - 21 wristband
        print("You may enter, but you need to wear a wristband ")
    
    elif age >= 21:
        # 21+ drink, normal entry
        print("You may enter and allowed to drink")

    else:
        # too young, sorry
        print("Go home to your mummy")

else:
    print("Please enter your age: ")

