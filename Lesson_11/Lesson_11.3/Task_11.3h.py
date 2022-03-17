list = []
for _ in range(int(input())):
    list.append(input())
key = int(input()) - 1
for element in list:
    if key < len(element):
        print(element[key], end='')
