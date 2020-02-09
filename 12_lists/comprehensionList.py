#list comprehension
numbers = [num*10 for num in range(1,6)]
print(numbers) # [10, 20, 30, 40, 50]


# list comprehension upper case for first character of names
friends = ['nam', 'nikki', 'pebbles']
names = [char[0].upper() for char in friends]
print(names)


# list comprehension upper case
name = 'nam'
upperName = [char.upper() for char in name]
print(name) # nam
print(upperName) # ['N', 'A', 'M']

# looping
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2, 4, 6, 8, 10]

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
