number1, number2, number3 = int(input()),  int(input()),  int(input())
max_number = max(number1, number2, number3)
min_number = min(number1, number2, number3)
print(max_number, number1 + number2 + number3 - max_number - min_number, min_number, sep='\n')
