my_dict = {'Andrej': 1991, 'Sergej': 1989, 'Anna': 1995}
print(my_dict)
print('Год рождения :', my_dict['Anna'])
print('Наличие в списке:', my_dict.get('Oleg'))
my_dict.update({'Ivan': 2001,
                'Polina': 1992})
print(my_dict)
print(my_dict.pop('Sergej'))
print(my_dict)

my_set = {25, 2.5, 'abc', 2.5, '123'}
print(my_set)
my_set.add(123)
my_set.add(True)
print(my_set)
my_set.discard(25)
print(my_set)