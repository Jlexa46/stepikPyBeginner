number = int(input())
if (number // 1000 + number % 10) == ((number % 1000) // 100 - (number % 100) // 10):
    print('ДА')
else:
    print('НЕТ')

# modified
# number = int(input())
# print('ДА' if (number // 1000 + number % 10) == ((number % 1000) // 100 - (number % 100) // 10) else 'НЕТ')
