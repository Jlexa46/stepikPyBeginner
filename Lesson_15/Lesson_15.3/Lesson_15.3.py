# Магический шар 8
# Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить
# пользователя задать некий вопрос, чтобы случайным образом на него ответить.

# Составляющие проекта:
#     - Целые числа (тип int);
#     - Переменные;
#     - Ввод / вывод данных (функции input() и print());
#     - Условный оператор (if/elif/else);
#     - Цикл while;
#     - Бесконечный цикл;
#     - Операторы break, continue;
#     - Работа с модулем random для генерации случайных чисел.

# Варианты ответов
# Традиционно шар имеет 20 ответов, которые можно разделить на четыре группы.
# Положительные:
#     Бесспорно
#     Предрешено
#     Никаких сомнений
#     Определённо да
#     Можешь быть уверен в этом
# Нерешительно положительные:
#     Мне кажется - да
#     Вероятнее всего
#     Хорошие перспективы
#     Знаки говорят - да
#     Да
# Нейтральные:
#     Пока неясно, попробуй снова
#     Спроси позже
#     Лучше не рассказывать
#     Сейчас нельзя предсказать
#     Сконцентрируйся и спроси опять
# Отрицательные:
#     Даже не думай
#     Мой ответ - нет
#     По моим данным - нет
#     Перспективы не очень хорошие
#     Весьма сомнительно

# Примечания
# Примечание 1. Внутри магического шара есть ёмкость с тёмной жидкостью, например, чернилами. В жидкости плавает фигура
# с 20 гранями, на каждой из них нанесено по одному ответу.
# Примечание 2. Многогранник с 20 гранями называется икосаэдр.


# Заголовок программы
# 1. Подключите модуль random;
# 2. Создайте список answers, содержащий 20 потенциальных ответов (Бесспорно, Предрешено, и т.д.).

# Приветствие пользователя
# 1. Выведите текстовое сообщение: 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.';
# 2. Уточните как зовут пользователя;
# 3. Выведите слова приветствия, например, 'Привет Тимур'.

# Основной цикл программы
# 1. Организуйте цикл, который будет запрашивать у пользователя данные;
# 2. Запросите у пользователя вопрос;
# 3. Выведите случайный ответ с помощью функции choice() передав список answers в качестве аргумента;
# 4. Уточните у пользователя, хочет ли он задать еще один вопрос, если да, то вернитесь в основной цикл программы,
#   если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.