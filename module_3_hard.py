
def sum_data(*args):
    summa = 0

    while args:
        if type(args) == tuple:
            args = list(args)
        a = args.pop()
        if isinstance(a, (int, float)):
            summa += a
        if type(a) == str:
            summa += (len(a))
        if isinstance(a, (list, tuple, set)):
            summa += sum_data(*a)
        if type(a) == dict:
            summa += sum_data(*(list(a.values()) + list(a.keys())))
    return summa


print(sum_data([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]))

