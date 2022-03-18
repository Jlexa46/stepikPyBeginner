list = input().split()
for el in list:
    print(el[0] + '.', end='')

# modified
# print('.'.join([el[0] for el in input().split()]), end='.')
