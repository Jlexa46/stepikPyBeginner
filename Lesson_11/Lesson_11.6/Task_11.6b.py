list = [int(el) for el in input().split()]
max_element, min_element = list.index(max(list)), list.index(min(list))
list[max_element], list[min_element] = list[min_element], list[max_element]
print(*list)
