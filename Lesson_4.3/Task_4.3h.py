number = int(input())
if number == 0:
    print('зеленый')
elif 1 <= number <= 10 or 19 <= number <= 28:
    print('черный' if number % 2 == 0 else 'красный')
elif 11 <= number <= 18 or 29 <= number <= 36:
    print('красный' if number % 2 == 0 else 'черный')
else:
    print('ошибка ввода')
