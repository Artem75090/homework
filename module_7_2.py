def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    cursor = []
    for i in range(len(strings)):
        cursor.append(file.tell())
        file.write(strings[i] + '\n')
    file = open(file_name, 'r', encoding='utf-8')
    strings_positions ={}
    n = 0
    for i in file:
        strings_positions[(n+1, cursor[n])] = i[0:-1]
        n += 1
    file.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
