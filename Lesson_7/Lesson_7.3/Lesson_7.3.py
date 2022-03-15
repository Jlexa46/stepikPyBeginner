# Подсчет количества
# Напишем программу, которая считывает 10 чисел и определяет сколько из них больше 10
counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter += 1
print('Было введено', counter, 'чисел, больших 10.')

# Подсчет количества очень частый сценарий. Он состоит из 2х шагов:
# 1. Создание переменной счетчика и придание ей первоначального значения counter = 0
# 2. Увеличение переменной счетчика на 1: counter = counter + 1
# Часто при написании программ требуется использовать несколько счетчиков

counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

# Пример подсчета количества чисел из диапазона [1; 100], квадрат которых оканчивается на 4
counter = 0
for i in range(1, 101):
    if i ** 2 % 10 == 4:
        counter = counter + 1
print(counter)

# Вычисление суммы и произведения
# Напишем программу, которая считывает 10 чисел и определяет сумму тех из них, которые больше 10
total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)

# Подсчет суммы состоит из 2х шагов:
# 1. Создание переменной сумматора и придание ей первоначального значения total = 0
# 2. Увеличение переменной сумматора на нужное число: total = total + num

# Напишем программу, которая считает сумму натуральных чисел от 1 до 100
total = 0
for i in range(1, 101):
    total = total + i
print('Сумма равна', total)

# Напишем программу, которая запрашивает 10 чисел и находит их среднее значение
total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)

# Обмен значений переменных
# Во многих языках программирования для обмена значений используют 3 переменные, для обмена значений между 2 переменными
x = 5
y = 10

temp = x
x = y
y = temp

# В Python есть более простой способ
x, y = y, x

# Сигнальные метки
# Используется, когда надо чтобы одна чать программы узнала, о происходящем в другой части программы

# Напишем программу, определяющую, что натуральное число является простым
num = int(input())
flag = True
for i in range(2, num):
    if num % i == 0:  # если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
if num == 1:
    print('Это единица, оне не просто и не состовная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

# Максимум и минимум
# Напишем программу, которая считывает 10 положительных чисел и находит среди ний наибольшее число
largest = -1
for i in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)

# Расширенные операторы присваивания
# x += 1 сокрашенная запись x = x + 1
# x -= 1 сокрашенная запись x = x - 1
# x *= 1 сокрашенная запись x = x * 1
# x /= 1 сокрашенная запись x = x / 1
# x //= 1 сокрашенная запись x = x // 1
# x %= 1 сокрашенная запись x = x % 1