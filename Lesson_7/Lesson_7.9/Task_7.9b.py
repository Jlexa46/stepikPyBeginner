number = int(input()) * 2
for i in range(1, number + 1, 2):
    liner = 1
    for j in range(0, i):
        print(liner, end='')
        liner = (liner + 1) if j < (i // 2) else (liner - 1)
    print()
