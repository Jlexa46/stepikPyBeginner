# Создание списков
# Для того, чтобы создать список состоящий из 10 нулей мы можем использовать следующий код:
zeros = []
for i in range(10):
    zeros.append(0)

# В Python, однако есть более простой и компактный способ для создания такого списка. Мы можем использовать оператор
# умножения списка на число:
zeros = [0] * 10

# Для создания списков, заполненных по более сложным правилам нам приходится явно использовать цикл for.
numbers = []
for i in range(10):
    numbers.append(i)


# Списочные выражения
# В Python есть механизм для создания списков из неповторяющихся элементов. Такой механизм называется — списочное
# выражение (list comprehension).
numbers = [i for i in range(10)]


# Примеры использования списочных выражений
# 1. Создать список, заполненный 10 нулями можно и при помощи списочного выражения:
zeros = [0 for i in range(10)]

# 2. Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
squares = [i ** 2 for i in range(10)]

# 3. Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
cubes = [i ** 3 for i in range(10, 21)]

# 4. Создать список, заполненный символами строки:
chars = [c for c in 'abcdefg']
print(chars)


# Считывание входных данных
# При решении многих задач из предыдущих уроков мы считывали начальные данные (строки, числа) и заполняли ими список.
# С помощью списочных выражений процесс заполнения списка можно заметно сократить.
lines = [input() for _ in range(int(input()))]

# Если требуется считать список чисел, то необходимо добавить преобразование типов:
numbers = [int(input()) for _ in range(int(input()))]

# Списочные выражения часто используются для инициализации списков. В Python не принято создавать пустые списки,
# а затем заполнять их значениями, если можно этого избежать.

# Условия в списочном выражении
# В списочных выражениях можно использовать условный оператор.
# Например, если требуется создать список четных чисел от 0 до 20, то мы можем написать такой код:
evens = [i for i in range(21) if i % 2 == 0]

# Важно: для того, чтобы получить список, состоящий из четных чисел, лучше использовать функцию range(0, 21, 2).
# Предыдущий пример приведен для демонстрации возможности использования условий в списочных выражениях.

# Вложенные циклы
# В списочном выражении можно использовать вложенные циклы.
numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)  # [0, 1, 0, 2, 0, 3, 0, 4]
