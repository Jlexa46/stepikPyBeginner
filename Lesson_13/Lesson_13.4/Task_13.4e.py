# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
