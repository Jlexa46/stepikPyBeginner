number1, number2, number3 = int(input()), int(input()), int(input())
print(number1 if number2 < number1 < number3 or number3 < number1 < number2 else number2 if number1 < number2 < number3 or number3 < number2 < number1 else number3)
