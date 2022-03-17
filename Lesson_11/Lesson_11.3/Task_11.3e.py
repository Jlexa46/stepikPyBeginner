list, number = [], int(input())
for i in range(1, number + 1):
    if number % i == 0:
        list.append(i)
print(list)
