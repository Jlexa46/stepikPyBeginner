func = []
for _ in range(int(input())):
    func.append(int(input()))
    print(func[-1])
print()
for el in func:
    print(el ** 2 + 2 * el + 1)
