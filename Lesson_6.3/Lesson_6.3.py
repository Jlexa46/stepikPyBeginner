# Строковый тип данных
# Для создания строковой переменной (литерала), мы должны заключить неоьбходимы текст в кавычки.

s1 = 'Python rocks!'
s2 = "Python rocks!"
s = input()  # переменная s имеет строковый тип str

# Длина строки
# Чтобы посчитать длину строки используеи встроенную функцию len()

s1 = 'abcdef'
length1 = len(s1)
length2 = len('Pyrhon rocks!')
print(length2)  # 6
print(length2)  # 13

# Преобразование чисел в строку
num1 = 1777   # целое число
num2 = 17.77  # число с плавающей точкой
s1 = str(num1)  # преобразование целого числа в строку
s2 = str(num2)  # преобразование числа с плавающей точкой в строку

# Конкатенация строк
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)  # abbc
print(s2)  # bcab
print(s3)  # abbcbcab!!

# Умножение строки на число
s = 'Hi' * 4
print(s)  # HiHiHiHi
print('-' * 75)

# Примечание. Тройный ковычки использются для многострочного текста
text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''

# Оператор in
# Позволяет проверить, что одна строка находится внутри другой
s = input()
if 'a' in s:
    print('Введена строка содержит символ а')
else:
    print('Введена строка не содержит символ а')

# Вместе с оператором in, можно использовать логический оператор not
s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')

