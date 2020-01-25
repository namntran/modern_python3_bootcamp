times = input ("how many times to I have to tell you? ")
times = int(times) #convert string into integer

for time in range(times):
     print("Clean up your room!")
     if time >=4:
        print("don't you even listen anymore?")
        break
