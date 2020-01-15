# ask for age
age = input("How old are you: ")
if age != "":
    if int(age) >= 18 and int(age) < 21:
        # 18 - 21 wristband
        print("You may enter, but need a wristband ")
    
    elif int(age) >= 21:
        # 21+ drink, normal entry
        print("You may enter and allowed to drink")

    else:
        # too young, sorry
        print("Go home to your mummy")

else:
    print("Please enter your age: ")

