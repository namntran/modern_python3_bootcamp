#program prints unlucky numbers
#refactor program to have only one print statement for less duplication
for n in range(1,21):
    if n == 4 or n == 13:
        # print(f"{n} is unlucky")
        state = "unlucky"
    elif n % 2 == 0:
        # print(f"{n} is even")
        state = "even"
    else:
        # print(f"{n} is odd")
        state = "odd"
    print(f"{n} is {state}")
   

   


