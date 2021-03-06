# Функции
# В самом начале курса вам было предложено решить задачу, в которой требовалось изобразить звездный прямоугольник
# размерами 5×7 (5 строк и 7 столбцов).

# Наш первый вариант кода выглядел примерно так:
print('*******')
print('*******')
print('*******')
print('*******')
print('*******')

# Далее мы изучили оператор умножения строки на число (оператор повторения) и написали бы код:
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)

# Ну и наконец, мы изучили циклы, после чего код принял бы вид:
for _ in range(5):
    print('*' * 7)

# А теперь представим, что таких прямоугольников нужно изобразить не один, а несколько, скажем 3 штуки.
for _ in range(5):
    print('*' * 7)
print()
for _ in range(5):
    print('*' * 7)
print()
for _ in range(5):
    print('*' * 7)

# И хотя предыдущий код полностью решает поставленную задачу, он не лишен недостатков.
# Во-первых, он довольно громоздкий из-за повторения части кода, отвечающей за вывод прямоугольника.
# Во-вторых, если понадобится изменить размеры прямоугольника, придется менять их трижды, в каждой части кода,
# выводящей прямоугольник.
# Вместо повторения кода для вывода прямоугольника, можно перенести его в отдельную функцию и вызвать ее 3 раза.
def draw_box():
    for _ in range(5):
        print('*' * 7)

# Когда функция создана, чтобы увидеть результат ее работы, надо вызвать ее по имени:
draw_box()

# Теперь чтобы изобразить 3 прямоугольника можно написать код:
draw_box()
print()
draw_box()
print()
draw_box()

# Код стал короче, читабельнее (за счет удачного названия функции), а главное, если потребуются иные размеры
# прямоугольника, достаточно будет изменить только саму функцию draw_box().

# Именование функций
# Имена функциям назначаются точно так же, как переменным. Имя функции должно быть достаточно описательным, чтобы любой,
# читающий ваш код, мог догадаться, что именно функция делает.
# Python и тут требует соблюдения тех же правил, что при именовании переменных:
#   1. в имени функции используются только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_);
#   2. имя функции не может начинаться с цифры;
#   3. имя функции по возможности должно отражать ее назначение;
#   4. символы верхнего и нижнего регистра различаются.

# Поскольку функции выполняют действия, большинство программистов предпочитает в именах функций использовать глаголы.
# Например:
#   функцию, которая рисует прямоугольник можно назвать draw_box();
#   функцию, которая печатает чек, можно назвать print_check();
#   функцию, которая вычисляет заработную плату до удержаний, можно назвать calculate_gross_рау().
# Каждое из этих имен дает описание того, что функция делает.

# Функции объявляются с помощью ключевого слова def (от слова define – определять). За ключевым словом def следуют
# название функции, круглые скобки (), и двоеточие :
# def название_функции():
#     блок_кода
