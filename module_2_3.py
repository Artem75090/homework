my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while len(my_list) > index:
    number = my_list[index]
    index = index + 1
    if number < 0:
        break
    elif number == 0:
        continue
    print(number)
