if input() == input():
    print('Пароль принят')
else:
    print('Пароль не принят')

# modified v1
# print('Пароль принят' if input() == input() else 'Пароль не принят')

# modified v2
# print(f"Пароль {'не ' if input() != input() else ''}принят")
