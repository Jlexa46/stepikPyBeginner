is_one_digit, number = True, int(input())
digit = number % 10
while number != 0:
    is_one_digit = False if digit != number % 10 else is_one_digit
    number //= 10
print('YES' if is_one_digit else 'NO')

# modified
# number = input()
# print('YES' if max(number) == min(number) else 'NO')
