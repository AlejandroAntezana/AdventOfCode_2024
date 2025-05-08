# Day 2: Red-Nosed Reports
from collections import UserList

with open("/home/code_zone/AdventCode2024/input_p2.txt") as archivo:
    levels = [level.strip() for level in archivo if level.strip()]
    # levels contains (in a list format) every line from the input text
test = levels[989:]
# print(test)
# print(len(levels))
secure_levels = 0
for level in levels:
    list_of_level = level.split()  # -> ['1','2','4','7'] / 4 5 2 4 5 6 / 62 63 60 60 60
    #print(list_of_level)
    length = len(list_of_level)
    if int(list_of_level[0]) < int(list_of_level[1]):
        for i in range(length - 1):
            if int(list_of_level[i]) < int(list_of_level[i + 1]):
                value = abs(int(list_of_level[i]) - int(list_of_level[i + 1]))
                if (not (value > 0 and value <= 3)):
                    break
                if (i + 1) == length - 1:
                    secure_levels += 1
            else:
                break
    elif int(list_of_level[0]) == int(list_of_level[1]):
        continue
    else:
        for i in range(length - 1):
            if int(list_of_level[i]) > int(list_of_level[i + 1]):
                value = abs(int(list_of_level[i]) - int(list_of_level[i + 1]))
                if (not (value > 0 and value <= 3)):
                    break
                if (i + 1) == length - 1:
                    secure_levels += 1
            else:
                break
print(secure_levels)
