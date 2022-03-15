number = int(input())
print(number, number * 2, number * 3, number * 4, number * 5, sep='---')

# modified v1
# number = int(input())
# print(*range(number, number * 6, number), sep='---')

# modified v2
# [print(number, number * 2, number * 3, number * 4, number * 5, sep='---') for number in [int(input())]]
