# Вложенные циклы
# Вложенный цикл расположен внутри еще одного цикла. Часы служат хорошим примером работы вложенного цикла.
# Секундная, минутная и часовая стрелки вращаются вокруг циферблата. Часовая стрелка смещается всего на 1 шаг для каждых
# 60 шагов минутной стрелки. И секундная стрелка должна сделать 60 шагов для 1 шага минутной стрелки. Это означает, что
# для каждого полного оборота часовой стрелки (12 шагов), минутная стрелка делает 720 шагов.

# Рассмотрим цикл, который частично моделирует электронный часы. Он показывает секунды от 0 до 59:
for seconds in range(60):
    print(seconds)

# Можно добавить переменную minutes и вложить цикл написанный выше внутрь еще одного цикла, который повторяется 60 раз:
for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)

# Для того, чтобы сделать модель законченной, можно добавить еще одну переменную для подсчета часов:
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

# Пример с часами подводит нас к нескольким моментам, имеющим отношение к вложенным циклам:
# - вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла;
# - вложенный циклы завершают свои итерации быстрее, чем внешние циклы;
# - для того чтобы получить общее количество итераций вложенного цикла, надо перемножить количество итераций всех циклов.

# Операторы break и continue во вложенных циклах
# Оператор break выполняет прерывание ближайшего цикла в котором он расположен. Аналогично, оператор continue осуществляет
# переход на следующую итерацию ближайшего цикла.
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)

# Использование вложенных циклов для решения уравнений
# Вложенные циклы можно использовать для решения уравнений с несколькими переменными. Зная, что решения (корни)
# уравнения являются натуральными (целыми) числами, несложно написать программу, содержащую вложенный цикл и
# перебирающую все возможные значения переменных.

# Решение задач
# Задача 1. Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения 12 * X + 13 * Y == 777
# Решение. Поскольку по условию числа X и Y являются натуральными, то X <= 64, Y <= 59. Напишем программу,
# которая перебирает всевозможные пары чисел (X; Y) и проверяет для них выполнение условий 12 * X + 13 * Y == 777
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)

# Задача 2. Найдите все пары натуральных чисел (и их количество) являющихся решением уравнения (X ** 2) + (Y ** 2) + (Z ** 2) == 2020
# Решение. Поскольку по условию числа X, Y и Z является натуральными, то X, Y, Z <= (2020 ** 0.5) = 45. Напишем программу,
# которая перебирает всевозможные тройки чисел (X; Y; Z) и проверяет для них условия X ** 2 + Y ** 2 + Z ** 2 == 2020
total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)