for i in range(int(input()), int(input()) + 1):
    print((str(i) + '\n') if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0) else '', end='')
