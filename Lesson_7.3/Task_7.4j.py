is_even = True
for i in range(10):
    if int(input()) % 2 != 0:
        is_even = False
print('YES' if is_even else 'NO')
