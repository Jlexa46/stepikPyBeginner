# объявление функции
def get_next_prime(num):
    n = num + 1
    while True:
        is_prime = True
        for i in range(2, n):
            is_prime = not (n % i == 0)
        if is_prime:
            break
        n += 1
    return n

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
