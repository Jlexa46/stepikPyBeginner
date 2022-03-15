s = input()
for c in s:
    if c in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')
