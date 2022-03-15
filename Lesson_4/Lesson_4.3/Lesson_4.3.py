# Вложенный оператор

# if условие1:
#       блок_кода
# else:
#       if условие2:
#           блок_кода
#       else:
#           if условие3:
#               блок_кода
#           ...

# Пример хорошо читаемого кода с вложенными условиями
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')

# Пример первода 100 бальной оценки в 5 бальную с вложенными условиями
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

# Каскадный условный оператор

# if условие1:
#   блок_кода
# elif условие2:
#   блок_кода
#...
#else:
#   блок_кода

# Пример первода 100 бальной оценки в 5 бальную с каскадными условиями
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

# Задача 1. Даны 3 целых числа. Определить, сколько среди них совпадающих.
# Способ 1. Использование вложенного условного оператора
a, b, c = int(input()), int(input()), int(input())
if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

# Способ 2. Использование каскадного условного оператора
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

# Способ 3. Использование каскадного условного оператора и логического оператора or
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)
