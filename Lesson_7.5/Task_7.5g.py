number, is_down = int(input()), True
digit = number % 10
while number != 0:
    is_down = False if digit > number % 10 else is_down
    digit, number = number % 10, number // 10
print('YES' if is_down else 'NO')

# modified
# number = int(input())
# while number % 10 <= number // 10 % 10:
#     number //= 10
# print('YES' if number < 10 else 'NO')
