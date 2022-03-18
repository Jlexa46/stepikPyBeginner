list = []
for _ in range(int(input())):
    list.append(input())
key = []
for _ in range(int(input())):
    key.append(input())
for el in list:
    is_find = True
    for k in key:
        if k.lower() not in el.lower():
            is_find = False
            break
    if is_find:
        print(el)
