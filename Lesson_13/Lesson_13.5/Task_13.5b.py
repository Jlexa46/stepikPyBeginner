# объявление функции
def is_prime(num):
    if num == 1:
        return False
    return True and not sum([i for i in range(2, num) if num % i == 0])

# # считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
