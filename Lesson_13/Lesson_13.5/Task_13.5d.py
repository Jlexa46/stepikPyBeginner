# объявление функции
def is_password_good(password):
    is_digit = is_upper = is_lower = False
    for c in password:
        if c.isupper(): is_upper = True
        if c.islower(): is_lower = True
        if c.isdigit(): is_digit = True
    return len(password) >= 8 and is_digit and is_lower and is_upper

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
