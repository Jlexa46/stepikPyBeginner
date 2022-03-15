total = 0
for i in range(1, int(input()) + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total += factorial
print(total)

# modified
# total = 0
# for i in range(1, int(input()) + 1):
#     from math import factorial
#     total += factorial(i)
# print(total)
