import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "!#$%&*+-=?@^_"

print('Чтобы сгенерировать пароль, мне нужно уточнить несколько вопросов:')
count = int(input('Сколько паролей необходимо сгенерировать? '))
length = int(input('Сколько символов должно быть в пароле? (рекомендуется - 8) '))
number_on = 'д' == input("Должен ли пароль содержать цифры [0-9]? ('д'-да,'н'-нет) ").strip()[0]
letters_upper_on = 'д' == input("Должен ли пароль содержать прописные буквы[A-Z]? ('д'-да,'н'-нет) ").strip()[0]
letters_lower_on = 'д' == input("Должен ли пароль содержать строчные буквы[a-z]? ('д'-да,'н'-нет) ").strip()[0]
punctuation_on = 'д' == input("Должен ли пароль содержать специальные симолы? ('д'-да,'н'-нет) ").strip()[0]
equals_letters_on = 'д' == input("Должен ли пароль содержать неоднозначные символы [il1Lo0O]? ('д'-да,'н'-нет) ").strip()[0]

chars = []
chars += digits if number_on else []
chars += lowercase_letters if letters_lower_on else []
chars += uppercase_letters if letters_upper_on else []
chars += punctuation if punctuation_on else []

if not equals_letters_on:
    chars = [c for c in chars if c not in 'il1Lo0O']


def generate_password(length, chars):
    return random.sample(chars, length)


for _ in range(count):
    print(*generate_password(length, chars), sep='')
