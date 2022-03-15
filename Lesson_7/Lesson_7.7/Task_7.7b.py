maximum = 1
total = 0
for i in range(10):
    x = int(input())
    if x < 0:
        total += x
        if x > maximum or maximum == 1:
            maximum = x
if maximum == 1:
    print('NO')
else:
    print(total)
    print(maximum)
