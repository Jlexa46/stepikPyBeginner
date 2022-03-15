total_star = total_plus = 0
for c in input():
    if c == '+':
        total_plus += 1
    if c == '*':
        total_star += 1
print('Символ + встречается', total_plus, 'раз')
print('Символ * встречается', total_star, 'раз')
