def all_variants(text):
    c = 1
    while True:
        a = 0
        b = c
        while True:
            yield text[a:b]
            a += 1
            b += 1
            if b == len(text) + 1:
                break
        if len(text[a:b]) == len(text) - 1:
            break
        c += 1

a = all_variants("abc")

for i in a:
    print(i)
