x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if ((x1 * 10 + y1) - (x2 * 10 + y2)) % 11 == 0:
    print('YES')
elif ((x1 * 10 + y1) - (x2 * 10 + y2)) % 9 == 0:
    print('YES')
else:
    print('NO')

# modified
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# print('YES' if (x1 - x2) ** 2 == (y1 - y2) ** 2 else 'NO')
