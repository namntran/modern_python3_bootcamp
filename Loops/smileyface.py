# print smiley face art

# for x in range(3):
#     for num in range(1,11): #nested loop
#         print("\U0001f600" * num)

# times = 1
# while times < 11:
#     print("\U0001f600" * times)
#     times += 1

# without string multiplication - ugly solution
for num in range(1,11): #nested loop
    count = 1
    smileys = ""
    while count < num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)