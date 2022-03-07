A, B, C = int(input()), int(input()), int(input())
print('YES' if (A + B) > C and (A + C) > B and (B + C) > A else 'NO')
