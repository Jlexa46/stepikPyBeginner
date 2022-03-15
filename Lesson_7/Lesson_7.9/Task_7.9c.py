a_border, b_border = int(input()), int(input())
max_total = max_devider = 0
for i in range(a_border, b_border + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if max_total <= total:
        max_total, max_devider = total, i
print(max_devider, max_total)
