import random


def is_valid(text):
    is_digit = text.isdigit()
    if is_digit:
        return 1 <= int(text) <= 99
    return False


def game():
    print('Добро пожаловать в числовую угадайку')

    number = random.randint(1, 100)
    count_of_try = 0

    while True:
        count_of_try += 1
        user_number = input('Введите число от 1 до 100 =')

        if not is_valid():
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue

        user_number = int(user_number)

        if user_number > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif user_number < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        else:
            print('Вы угадали, поздравляем!')
            print(f'Число было угадано за {count_of_try} попыток!')
            break

    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


def is_valid_answer():
    while True:
        answer = input('Желаете ли вы продолжить игру? (да - д, нет - н)')
        if answer[0].lower() == 'д':
            return True
        elif answer[0].lower() == 'н':
            break
        else:
            print("Не могу разобрать ваш ответ, введите 'д'- да, 'н' - нет")

    return False


new_game = True

while new_game:
    while True:
        game()
        if not is_valid_answer():
            break
