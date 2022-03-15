for i in range(1, int(input()) + 1):
    print(i, end='')
    for j in range(1, i + 1):
        print('+' if i % j == 0 else '', end='')
    print()
