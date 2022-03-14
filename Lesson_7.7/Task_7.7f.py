number = int(input())
product = 1
while number > 0:
    digit = number % 10
    product *= digit
    number //= 10
print(product)
