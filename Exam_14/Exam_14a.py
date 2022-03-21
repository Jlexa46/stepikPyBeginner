# объявление функции
def draw_triangle():
    print(*[' ' * (7 - i // 2) + '*' * i for i in range(1, 16, 2)], sep='\n')


# основная программа
draw_triangle()  # вызов функции