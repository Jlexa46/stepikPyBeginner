a, b = int(input()), int(input())
print(3 * pow((a + b), 3) + 275 * pow(b, 2) - 127 * a - 41)

# modified
# print((lambda a, b: 3*(a+b)**3+275*b*b-127*a-41)(int(input()), int(input())))
