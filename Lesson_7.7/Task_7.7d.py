number = int(input())
max_digit = -1
while number > 0:
    digit = number % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    number //= 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)
