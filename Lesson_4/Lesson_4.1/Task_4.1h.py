age = int(input())
if age <= 13:
    print('детство')
elif age <= 24:
    print('молодость')
elif age <= 59:
    print('зрелость')
else:
    print('старость')

# modified
# age = int(input())
# print('старость' if age > 59 else 'зрелость' if age > 24 else 'молодость' if age > 13 else 'детство')
