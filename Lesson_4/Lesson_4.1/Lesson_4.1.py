# Условный оператор if-else

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')

# (:) в конце строки с инструкцией if сообщает интерпретатору Python, что дальше находится блок команд.
# В блок команд входят все строки с отступом под строкой с инструкцией if, вплоть до следующей строки без отступа.

# Блок кода называют объединенные друг с другом строки. В Python блоки кода формируются при помощи отступов.

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

# Отступ - небольшое смещение строки кода вправо. В начале такой строки стоят пробелы, и поэтому она на несколько
# символов отстоит от края. По соглашению PEP 8 отступ формируется 4 пробелами.

# Оператор присваивания
num = 1992
s = 'I love Python'
name = 'Gvido'
temperature = 40

# Оператор сравнения
if answer == 'Python':
    pass

if name == 'Gvido':
    pass

if temperature == 40:
    pass

# В Python существует 6 основных операторов сравнения:
# if x > 7  если х больше 7
# if x < 7  если х меньше 7
# if x >= 7  если х больше либо равен 7
# if x <= 7  если х меньше либо равен 7
# if x == 7  если х равен 7
# if x != 7  если х не равен 7

num1 = int(input())
num2 = int(input())
if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:
    print(num1, 'равен', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

# Операторы сравнения можно объединять в цепочки
age = int(input())
if 3 <= age <= 6:
    print('Вы ребенок')

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('числа равны')
else:
    print('числа не равны')

# Операция равенства является транзитивной. Это означает, что если а == b и b == c, то из этого следует, что a == c.
# Из курса математики вам знакомы следующие примеры транзитивных операций:
# Отношение порядка: если a > b и b > c, то a > c;
# Параллельности прямых: если a || b и b || c, то a || c;
# Делимости: если a делится на b и b делится на c, то a делится на c.

# Операция (!=) является нетранзитивной. То есть из того, что a != b и b != c, вовсе не следует, что a != c.
if a != b != c:
    print('числа не равны')
else:
    print('числа равны')

# Задача 1. Написать программу выводящую при вводе строки Python ответ ДА, иначе НЕТ.
word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')

# Задача 2. Написать программу выводящую при ввод одинаковых цифр двузначного числа ответ ДА, иначе НЕТ.
num = int(input())
last_digit = num % 10
first_digit = num // 10
if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')

# Задача 3. Написать программу принимающая 3 числа и подсчета количества четных чисел.
num1, num2, num3, counter = int(input()), int(input()), int(input()), 0
if num1 % 2 == 0:
    counter += 1
if num2 % 2 == 0:
    counter += 1
if num3 % 2 == 0:
    counter += 1
print(counter)