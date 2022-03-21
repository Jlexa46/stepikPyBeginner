list = input().split()
print('+'.join(list), '=', sum([int(i) for i in list]), sep='')
