from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])
food = input("name a food type?")

if food == 'apple' or food == 'grape':
    print ("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")