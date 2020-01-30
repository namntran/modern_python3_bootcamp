# #use a while loop to take advantage of the index of each item in list
# numbers = [1,2,3,4]
# i = 0 #set value of index (i) in list [1,2,3,4] to 0

# while i < len(numbers):
#     print(numbers[i])
#     i += 1

colours = ["red", "yellow", "purple", "green"]

index = 0
while index < len(colours):
    print(f"{index}: {colours[index]}")
    index += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()
    print(result)

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
    print(result)
result = result.upper()
 