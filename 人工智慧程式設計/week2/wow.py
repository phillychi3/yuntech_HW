a, b = [[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]]
c = [[0] * 3, [0] * 3, [0] * 3]
d = [[0] * 3] * 3
c[1][1] = 9
d[1][1] = 9
print(a, b, c, d, sep="\n")

for i in range(3):
    for j in range(3):
        s = 0
        for k in range(2):
            s += a[i][k] * b[k][j]
            c[i][j] = s
print(c)
