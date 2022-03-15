number = int(input())
while number != 0:
    last_number, number = number % 10, number // 10
    print(last_number)

# modified
# [print(i) for i in list(input())[::-1]]
