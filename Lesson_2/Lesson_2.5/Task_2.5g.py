number = int(input())
digit1 = number % 10
digit2 = (number % 100) // 10
digit3 = number // 100
print('Сумма цифр = ', digit1 + digit2 + digit3, '\nПроизведение цифр = ', digit1 * digit2 * digit3, sep='')

# modified v1
# number = int(input())
# print('Сумма цифр = ', number % 10 + (number % 100) // 10 + number // 100, '\nПроизведение цифр = ', (number % 10) * ((number % 100) // 10) * (number // 100), sep='')

# modified v2
# [print(f'Сумма цифр = {digit1 + digit2 + digit3}\nПроизведение цифр = {digit1 * digit2 * digit3}') for digit1, digit2, digit3 in [[int(num) for num in input()]]]
