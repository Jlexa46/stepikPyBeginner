# Параметр разделителя sep

# Вывод текста по умолчанию
print('a', 'b', 'c')    # a b c
print('d', 'e', 'f')    # d e f

# Вывод текста с разделителем
print('a', 'b', 'c', sep='*')     # a*b*c
print('d', 'e', 'f', sep='**')    # d**e**f

# Параметр окончания end
print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')    # a b c@d e f@@

print()

# Пример использования sep и end одновременно
print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!') # a*b*cfinishd**e**f^__^g+h+i%j-k-l#m/n/o!


