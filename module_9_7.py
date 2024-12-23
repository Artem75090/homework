def is_prime(func):
    def wrapper(a, b, c):
        flag = True
        res_sum_three = func(a, b, c)
        for i in range(2, res_sum_three):
            if res_sum_three % i == 0:
                flag = False
                break
        if flag:
            print(f"Простое")
        else:
            print(f"Составное")
        return res_sum_three

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
