items = ["socks", "mug", "pot", "kibble"]
# items.clear()
print(items)
items.pop()
print(items)

last_items = items.pop()
print(items)
print(last_items)

first_list = [1, 2, 3, 4]
first_list.pop()
print(first_list)
first_list.pop(1) #remove item at index 1
print(first_list)

names = ["colt", "blue", "arya", "lena", "colt", "selena", "pablo"]
print(names)
names.remove("blue")
print(names)
names.remove("colt")
print(names)