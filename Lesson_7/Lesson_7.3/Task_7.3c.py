import math
total, n = 0, int(input())
for i in range(1, n + 1):
    total += 1 / i
print(total - math.log(n))
