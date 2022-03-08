number = int(input())
if number % 2 != 0:
    print('YES')
elif number % 2 == 0 and 2 <= number <= 5:
    print('NO')
elif number % 2 == 0 and 6 <= number <= 20:
    print('YES')
elif number % 2 == 0 and number > 20:
    print('NO')
