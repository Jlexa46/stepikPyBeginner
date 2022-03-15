number = int(input())
digit3 = number % 10
digit2 = (number % 100) // 10
digit1 = number // 100
print(
    digit1, digit2, digit3, '\n',
    digit1, digit3, digit2, '\n',
    digit2, digit1, digit3, '\n',
    digit2, digit3, digit1, '\n',
    digit3, digit1, digit2, '\n',
    digit3, digit2, digit1, sep=''
)
