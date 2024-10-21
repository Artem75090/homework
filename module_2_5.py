def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        q = []
        matrix.append(q)
        for y in range(m):
            q.append(value)
    return matrix
print(get_matrix(4, 2, 123))


