list = [int(el) for el in input().split()]
list.sort()
print(*list)
list.sort(reverse=True)
print(*list)
