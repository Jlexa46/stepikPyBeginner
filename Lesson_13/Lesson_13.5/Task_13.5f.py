# объявление функции
def is_palindrome(text):
    s = [c for c in text.lower() if c not in ' !.-?,#$']
    if len(s) % 2 == 0:
        return s[:len(s) // 2 - 1] == s[len(s):len(s) // 2:-1]
    else:
        return s[:len(s) // 2] == s[len(s):len(s) // 2:-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
