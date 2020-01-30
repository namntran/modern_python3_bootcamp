#insert an item at a given position
first_list = [1, 2, 3, 4]
first_list.insert(2, 'Hi!')
print(first_list)

first_list.insert(-1, 'The end!')
print(first_list)

first_list.insert(len(first_list), "Last")
print(first_list)