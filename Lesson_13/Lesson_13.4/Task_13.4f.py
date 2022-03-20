# объявление функции
def merge(list1, list2):
    list = list1 + list2
    list.sort()
    return list

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
print(merge(numbers1, numbers2))
