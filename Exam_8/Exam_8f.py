n = int(input())
count_3 = 0
last_digit = n % 10
count_last_digit = 0
count_odd = 0
count_digit_more_5 = 0
product_digit_more_7 = 1
count_digit_0_or_5 = 0
while n != 0:
    digit = n % 10
    if digit == 3:
        count_3 += 1
    if last_digit == digit:
        count_last_digit += 1
    if digit % 2 == 0:
        count_odd += 1
    if digit > 5:
        count_digit_more_5 += digit
    if digit > 7:
        product_digit_more_7 *= digit
    if digit == 5 or digit == 0:
        count_digit_0_or_5 += 1
    n //= 10
print(count_3,
      count_last_digit,
      count_odd,
      count_digit_more_5,
      product_digit_more_7,
      count_digit_0_or_5,
      sep='\n')
