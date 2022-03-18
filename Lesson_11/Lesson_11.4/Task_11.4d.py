list = []
for _ in range(int(input())):
    s = input()
    if s not in list:
        list.append(s)
print(*list, sep='\n')
