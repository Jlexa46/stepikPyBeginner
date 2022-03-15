for i in range(int(input()), int(input()) + 1):
    is_simple = True
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_simple = False
            break
    if is_simple:
        print(i)
