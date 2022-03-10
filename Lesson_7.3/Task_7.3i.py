max_1, max_2 = 0, 0
for i in range(int(input())):
    num = int(input())
    if max == 0 and i == 0 or max_1 < num:
        max_1, max_2 = num, max_1
    else:
        if max_2 < num:
            max_2 = num
print(max_1, max_2, sep='\n')
