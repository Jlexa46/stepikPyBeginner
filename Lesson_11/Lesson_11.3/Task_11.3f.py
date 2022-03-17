list, previous = [], False
for _ in range(int(input())):
    if previous == False:
        previous = int(input())
        continue
    number = int(input())
    list.append(previous + number)
    previous = number
print(list)