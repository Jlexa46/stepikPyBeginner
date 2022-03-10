total = 1
for _ in range(10):
    num = int(input())
    total *= num if num > 0 else 1
print(total)
