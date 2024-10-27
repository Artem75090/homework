def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(False)
print_params(12, 21)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 123, 'str']
values_dict = {'a': 'значение', 'b': 321, 'c': 555}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, False]
print_params(*values_list_2, 42)

