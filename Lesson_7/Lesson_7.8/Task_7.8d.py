number = int(input())
for i in range(number):
    for j in range(0, (i + 1) if i < (number // 2) else number - i):
        print('*', end='')
    print()
