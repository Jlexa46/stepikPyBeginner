list = [int(el) for el in input().split('.')]
for el in list:
    if 0 > el or el > 255:
        print('НЕТ')
        break
else:
    print('ДА')

# modified
# print('ДА' if all(0 <= int(ip) <= 255 for ip in input().split('.')) else 'НЕТ')
