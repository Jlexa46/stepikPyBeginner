counter = 0
for _ in range(int(input())):
    s = input()
    if s.count('11') >= 3:
        counter += 1
print(counter)
