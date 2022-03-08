number1, number2, operator = int(input()), int(input()), input()
if not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
    print('Неверная операция')
elif operator == '/' and number2 == 0:
    print('На ноль делить нельзя!')
else:
    if operator == '*':
        print(number1 * number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '+':
        print(number1 + number2)
    else:
        print(number1 - number2)
