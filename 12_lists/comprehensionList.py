#list comprehension with conditional logic
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)

#list comprehension convert list of integers to strings
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
string_list = [str(num) for num in numbers]
print(string_list)

#list comprehension - generate numbers 1-5 and multiply them by 10
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
 