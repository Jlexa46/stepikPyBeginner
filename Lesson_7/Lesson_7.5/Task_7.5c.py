number = int(input())
maximal_digit, minimal_digit = 0, 9
while number != 0:
    last_digit, number = number % 10, number // 10
    maximal_digit = last_digit if last_digit > maximal_digit else maximal_digit
    minimal_digit = last_digit if last_digit < minimal_digit else minimal_digit
print('Максимальная цифра равна ', maximal_digit, '\nМинимальная цифра равна ', minimal_digit, sep='')

# modified
# number = int(input())
# maximal_digit, minimal_digit = 0, 9
# while number != 0:
#     minimal_digit, maximal_digit = min(minimal_digit, number % 10), max(maximal_digit, number % 10)
#     number //= 10
# print('Максимальная цифра равна ', maximal_digit, '\nМинимальная цифра равна ', minimal_digit, sep='')
