total = 0
for i in range(int(input()) + 1):
    total += i if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8 else 0
print(total)
