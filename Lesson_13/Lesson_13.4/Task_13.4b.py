# объявление функции
def get_days(month):
    return 28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
