total = 0
for i in range(int(input()), int(input()) + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1
print(total)
