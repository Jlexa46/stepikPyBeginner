number1, number2, number3 = int(input()), int(input()), int(input())
print((number1 if number1 > 0 else 0) + (number2 if number2 > 0 else 0) + (number3 if number3 > 0 else 0))

# modified
# number1, number2, number3 = int(input()), int(input()), int(input())
# print((number1 > 0) * number1 + (number2 > 0) * number2 + (number3 > 0) * number3)
