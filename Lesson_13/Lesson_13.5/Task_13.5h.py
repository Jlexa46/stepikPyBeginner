# объявление функции
def is_correct_bracket(text):
    total = 0
    for bracket in text:
        if total == 0 and bracket == ')':
            return False
        total += 1 if bracket == '(' else -1 if bracket == ')' else 0
    return True if total == 0 else False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
