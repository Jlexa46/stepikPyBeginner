counter, number = 1, int(input())
for i in range(number + 1):
    for j in range(i):
        print(counter, end=' ')
        counter += 1
    print()
