def print_digit_sum(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    print(total)


print_digit_sum(int(input()))

# modified
# def print_digit_sum(num):
#     print(sum(int(i) for i in str(num)))
# print_digit_sum(int(input()))
