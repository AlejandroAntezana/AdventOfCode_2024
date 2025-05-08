# Day 2: Red-Nosed Reports
with open("/home/code_zone/AdventCode2024/input_p2.txt") as archivo:
    levels = [level.strip() for level in archivo if level.strip()]
    # levels contains (in a list format) every line from the input text
secure_levels = 0

list_of_level = levels[0].split()  # -> ['1','2','4','7']
length = len(list_of_level)
for i in range(length - 1):
        if list_of_level[i] < list_of_level[i + 1]: #ascendente
                value = abs(int(list_of_level[i]) - int(list_of_level[i + 1]))
                if (not (value > 0 and value <= 3)):
                        break;
                if(i+1)==length-1:
                        secure_levels += 1
        elif(list_of_level[i] > list_of_level[i + 1]): #descendente
                value = abs(int(list_of_level[i]) - int(list_of_level[i + 1]))
                if (not (value > 0 and value <= 3)):
                        break;
                if(i+1)==length-1:
                        secure_levels += 1
        else:
                break;
print(secure_levels)
