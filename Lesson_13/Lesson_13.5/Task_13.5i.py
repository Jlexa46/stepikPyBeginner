# объявление функции
def convert_to_python_case(text):
    s = text
    for i in range(1, len(s)):
        if ord(s[i]) in range(65, 65 + 26):
            s = s[:i] + '_' + s[i].lower() + s[i + 1:]
    return s[0].lower() + s[1:]


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# modified
# def convert_to_python_case(text):
#     return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()
# txt = input()
# print(convert_to_python_case(txt))
