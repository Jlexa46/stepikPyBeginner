def draw_triangle(fill, base):
    print(*[fill * i for i in range(1, ((base + 1) // 2) + 1)], sep='\n')
    print(*[fill * i for i in range((base // 2), 0, -1)], sep='\n')


draw_triangle(input(), int(input()))
