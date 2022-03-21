# объявление функции
def is_pangram(text):
    s = text.replace(' ', '').lower()
    alphabet = [False for _ in range(26)]
    for c in s:
        alphabet[ord(c) - 97] = True
    return min(alphabet)


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
