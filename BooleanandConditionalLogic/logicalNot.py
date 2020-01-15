age = int(input("What is your age?"))
# age 2-8 years is $2 tickets
# age 65 years + is $5 tickets
# everyone else is $10 tickets

if not ((age >= 2 and age <= 8) or age >= 65 or age <2):
    print("you pay $10 dollars and not entitled to discount")
elif age >= 65:
    print("you pay $5 and are entiled to senior discount")
elif age >= 2 and age <= 8:
    print("you pay $2 and are entitled to child discount")
else:
    print("please don't cry during the movie")
