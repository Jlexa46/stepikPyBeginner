# объявление функции
def is_magic(date):
    list = [int(i) for i in date.split('.')]
    return list[0] * list[1] == list[2] % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
