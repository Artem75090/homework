n = int(input('Введите число: '))
w =[]
for i in range(3, n + 1):
    if n % i ==0:
        w.append(i)
result = []
a = 1
for j in range(n):
    b = 1
    for r in range(n):
        for z in range(len(w)):
            if a + b == w[z] and a != b and a < b:
                result.append(a)
                result.append(b)
        b += 1
    a += 1
print('Пароль: ', result)