a, b, c = len(input()), len(input()), len(input())
print('YES' if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0 else 'NO')
