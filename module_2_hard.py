n = int(input('Введите число: '))
w =[]
for i in range(3, n + 1):
    if n % i ==0:
        w.append(i)
result = []
a = 1
for j in range(1, 20):
    b = 1
    for r in range(1, 20):
        b += 1

        for z in range(len(w)):
            if a + b == w[z] and a != b and a < b:
                result.append(a)
                result.append(b)
    a += 1
print('Пароль: ', result)




