second_digit, number = 0, int(input())
while number != 0:
    second_digit = (number % 10) if number >= 10 else second_digit
    number //= 10
print(second_digit)
