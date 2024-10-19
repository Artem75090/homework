numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    y = 0
    for w in range(1, i + 1):
        if i % w == 0:
            y += 1
    if y <= 1:
        continue
    elif y == 2:
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)
