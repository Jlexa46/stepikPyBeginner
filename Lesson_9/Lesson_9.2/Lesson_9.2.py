# Срезы строк
# Иногда нужно бывает работать с целыми частями строки, в таком случае мы используем срезы (slices).
# Срезы похожи на комбинацию индексации и функции range()
s = 'abcdefghij'

# Положительные индексы 0   1   2   3   4   5   6   7   8   9
# Строка                a   b   c   d   e   f   g   h   i   j
# Отрицательные индексы -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# С помощью среза мы можем получить несколько символов исходной строки, создав диапазон индексов разделенных двоеточием s[x:y]
print(s[2:5])  # cde
print(s[0:6])  # acdef
print(s[2:7])  # cdefg

# Срез до конца, от начала
# Если опустить второй параметр в срезе s[x:] (но поставить двоеточие), то срез берется до конца строки.
# Аналогично если опустить первый параметр s[:y], то можно взять срез от начала строки. Срез s[:] совпадает с самой строкой s
print(s[2:])  # cdefghij
print(s[:7])  # abcdefg

# Отриацательные индексы в срезе
# Мы также можем использовать отрицательные индексы для создания срезов. Как уже говорилось ранее,
# отрицательные индексы строки начинаются с -1 и отсчитываются до достижения начала строки.
# При использовании отрицательных индексов первый параметр среза должен быть меньше второго, либо должен быть пропущен.
print(s[-9:-4])  # bcdef
print(s[-3:])    # hij
print(s[:-3])    # abcdefg

# Шаг среза
# Мы можем передать в срез третий необязательный параметр, который отвечает за шаг среза.
# К примеру, срез s[1:7:2] создаст строку bdf состоящую из каждого второго символа
# (индексы 1, 3, 5, правая граница не включена в срез)

# Отрицательный шаг среза
# Если в качестве шага среза указать отрицательное число, то символы будут идти в обратном порядке
print(s[::-1])  # jihgfedcba
print(s[1:7:2])  # bdf
print(s[3::2])   # dfhj
print(s[:7:3])   # adg
print(s[::2])    # acegi
print(s[::-1])   # jihgfedcba
print(s[::-2])   # jhfdb

# Изменение символа строки по индексу
# Предположим, у нас есть строка s = 'abcdefghij' и мы хотим заменить символ с индексом 4 на 'X'.
# Можно попытаться написать код:
s = 'abcdefghij'
s[4] = 'X'

# Однако такой код не работает. В Python строки являются неизменяемыми,
# то есть мы не можем менять их содержимое с помощью индексатора.
# Если мы хотим поменять какой-либо символ строки s, мы должны создать новую строку.
# Следующий код использует срезы и решает поставленную задачу:
s = s[:4] + 'X' + s[5:]
