total, degree = 0, int(input())
while 1 <= degree and degree <= 5:
    total += 1 if degree == 5 else 0
    degree = int(input())
print(total)

# modified
# total, degree = 0, int(input())
# while degree in range(1, 6):
#     total, degree = total + (degree == 5), int(input())
# print(total)
