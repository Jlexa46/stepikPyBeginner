m, p, n = float(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m += m * (p / 100)
