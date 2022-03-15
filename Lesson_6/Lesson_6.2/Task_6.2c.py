number1, number2 = float(input()), float(input())
print(
    (number1 + number2) / 2,
    (number1 * number2) ** 0.5,
    (2 * number1 * number2) / (number1 + number2),
    ((number1 ** 2 + number2 ** 2) / 2) ** 0.5, sep='\n'
)
