# ask for age
age = input("How old are you: ")
if age:
    age = int(age)
    if age >= 21:
        print("You may enter and allowed to drink")
    
    elif age >= 18:
        print("You may enter, but you need to wear a wristband")

    else:
        print("Go home to your mummy")

else:
    print("Please enter your age: ")
