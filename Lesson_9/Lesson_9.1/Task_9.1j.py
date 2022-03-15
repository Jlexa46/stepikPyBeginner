total1 = total2 = 0
for c in input():
    if c.lower() in 'ауоыиэяюёе':
        total1 += 1
    if c.lower() in 'бвгджзйклмнпрстфхцчшщ':
        total2 += 1
print('Количество гласных букв равно ', total1, '\nКоличество согласных букв равно ', total2, sep='')
