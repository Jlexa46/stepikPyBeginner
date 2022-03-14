number = int(input())
while number > 9:
    number = number // 10 + number % 10
print(number)
