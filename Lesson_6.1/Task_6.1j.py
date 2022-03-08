number = int(input())
digit1 = number % 10
digit2 = number % 100 // 10
digit3 = number // 100
print('Число интересное' if digit1 + digit2 == digit3 or digit1 + digit3 == digit2 or digit2 + digit3 == digit1 else 'Число неинтересное')

# modified
# number = int(input())
# digit1, digit2, digit3 = number % 10, number % 100 // 10, number // 100
# print('Число интересное' if max(digit1, digit2, digit3) == digit1 + digit2 + digit3 - max(digit1, digit2, digit3) else 'Число неинтересное')
