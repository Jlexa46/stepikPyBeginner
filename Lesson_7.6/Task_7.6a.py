number = int(input())
for i in range(2, number + 1):
    if number % i == 0:
        print(i)
        break

# modified
# number, divider = int(input()), 2
# while number % divider:
#     divider += 1
# print(divider)
