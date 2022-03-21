list_1 = [int(i) for i in input().split()]
list_2 = [int(i) for i in input().split()]
print(*[list_1[i] + list_2[i] for i in range(len(list_1))])
