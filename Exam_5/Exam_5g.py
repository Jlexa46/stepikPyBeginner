x1, y1, x2, y2 = int(input()),  int(input()), int(input()), int(input())
if abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
    print('YES')
else:
    print('NO')
