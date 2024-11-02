list_data = []
def sum_data(*args):

    while args:
        if type(args) == tuple:
            args = list(args)
        a = args.pop()
        if isinstance(a, (int, float)):
            list_data.append(a)
        if type(a) == str:
            list_data.append(len(a))
        if isinstance(a, (list, tuple, set)):
            sum_data(*a)
        if type(a) == dict:
            sum_data(*(list(a.values()) + list(a.keys())))
    return (sum(list_data))


print(sum_data([[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]))