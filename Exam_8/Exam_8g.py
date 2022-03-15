num1 = num2 = num3 = num4 = num5 = 0
is_find = False
for i in range(50):
    if is_find:
        break
    for j in range(50):
        if is_find:
            break
        for k in range(50):
            if is_find:
                break
            for l in range(50):
                if is_find:
                    break
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    if i ** 3 + j ** 3 == k ** 3 + l ** 3:
                        num = i ** 3 + j ** 3
                        if num1 == 0:
                            num1 = num
                        if num1 != num and num2 == 0:
                            num2 = num
                        if num2 != num and num1 != num and num3 == 0:
                            num3 = num
                        if num3 != num and num2 != num and num1 != num and num4 == 0:
                            num4 = num
                        if num4 != num and num3 != num and num2 != num and num1 != num and num5 == 0:
                            num5 = num
                            is_find = True
print(num1, num2, num3, num4, num5, sep='\n')