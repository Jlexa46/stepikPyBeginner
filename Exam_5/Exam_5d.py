number = int(input())
if 1 <= number <= 10:
    print(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][number - 1])
else:
    print('ошибка')
