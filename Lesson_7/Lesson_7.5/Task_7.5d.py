number = int(input())
total, length, product, average, head, tail = 0, 0, 1, 0, 0, number % 10
while number != 0:
    last_digit, number = number % 10, number // 10
    total, length, product, head = total + last_digit, length + 1, product * last_digit, last_digit
print(total, length, product, total / length, head, head + tail, sep='\n')
