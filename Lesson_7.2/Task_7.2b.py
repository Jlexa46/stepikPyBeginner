m, n = int(input()), int(input())
for i in range(m, (n + 1) if m < n else n - 1, -1 if m > n else 1):
    print(i)
if m == n:
    print(m)
