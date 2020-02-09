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
