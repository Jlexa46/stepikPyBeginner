# Работа с целыми числами

num1 = 7            # num1 - это число
num2 = 10           # num2 - это число
num3 = num1 + num2  # num3 - это число
print(num3)         # Строки обозначаются в ковычках, числа без ковычек

# В Python как и в математичке можно совершать 4 основные операции (+, -, *, /).
# + сложение
# - вычитание
# * умножение
# / деление

a = 3
b = 2
print(a + b)    # 5
print(a - b)    # 1
print(a * b)    # 6
print(a / b)    # 1.5

# Порядок выполнение операций
num1 = 2 + 3 * 4
num2 = (2 + 3) * 4
print(num1)     # 14
print(num2)     # 20

# Первым выполняется Умножение или Деление, а потом уже Сложение или Вычитание

# Преобразование типов
s = '1992'
year = int(s)   # Преобразуем строку в число

num1 = input()
num2 = input()
print(num1 + num2)  # В этом случае происходит конкатенация строк

num1 = int(input())
num2 = int(input())
print(num1 + num2)  # А в этом уже сложение двух чисел

# Преобразование целого числа к строке
num = 17        # В этом случае число 17
s = str(17)     # В этом случае строка '17'

# В Python реализованна длинная арифметика, т.е., по сути, переменная целого типа не имеет ограничений по объему памяти
# Минус (-) может использоватся для обозначения отрицательных чисел
num1 = -6       # Унарный минус
num2 = 17 - 7   # Бинарный минус