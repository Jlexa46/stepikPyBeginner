# объявление функции
def is_valid_password(password):
    psw = [int(num) for num in password.split(':')]
    is_prime = True
    for i in range(2, int(psw[1] ** 0.5) + 1):
        if psw[1] % i == 0:
            is_prime = False
    return len(psw) == 3 and str(psw[0]) == str(psw[0])[::-1] and is_prime and psw[2] % 2 == 0

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

