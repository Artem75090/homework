def is_prime(func):
    def wrapper(a, b, c):
        is_prime = True
        res_sum_three = func(a, b, c)
        for i in range(2, res_sum_three):
            if res_sum_three % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"Простое")
            return res_sum_three
        else:
            print(f"Составное")
            return res_sum_three

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
