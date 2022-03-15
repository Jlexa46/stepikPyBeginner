s, total = input(), 0
while s != 'стоп' and s != 'хватит' and s != 'достаточно':
    total += 1
    s = input()
print(total)

# modified
# total = 0
# while input() not in ('стоп', 'хватит', 'достаточно'):
#     total += 1
# print(total)
