list = [int(el) for el in input().split()]
total_pairs = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            total_pairs += 1
print(total_pairs)
