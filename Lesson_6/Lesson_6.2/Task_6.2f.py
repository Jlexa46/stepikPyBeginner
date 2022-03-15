a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-1 * b - D ** 0.5) / (2 * a)
    x2 = (-1 * b + D ** 0.5) / (2 * a)
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
elif D == 0:
    print(-1 * (b / (2 * a)))
else:
    print('Нет корней')
