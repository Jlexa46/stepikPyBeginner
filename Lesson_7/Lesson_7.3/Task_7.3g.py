total, n = 0, int(input())
for i in range(1, n + 1):
    total += i if n % i == 0 else 0
print(total)
