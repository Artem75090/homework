def is_prime(func):
    def wrapper(a, b, c):
        counter = 0
        res_sum_three = func(a, b, c)
        for i in range(1, res_sum_three + 1):
            if res_sum_three % i == 0:
                counter += 1
        if counter == 2:
            return f"Простое \n{res_sum_three}"
        else:
            return f"Составное \n{res_sum_three}"

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)