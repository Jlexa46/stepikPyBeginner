list = []
for _ in range(int(input())):
    list.append(int(input()))
del list[1::2]
print(list)
