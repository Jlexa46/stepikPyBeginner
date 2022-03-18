list = []
for _ in range(int(input())):
    list.append(input())
key = input().lower()
for el in list:
    if key in el.lower():
        print(el)
