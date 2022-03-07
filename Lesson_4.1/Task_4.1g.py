number1, number2, number3, number4 = int(input()), int(input()), int(input()), int(input())
if number1 <= number2 and number1 <= number3 and number1 <= number4:
    print(number1)
else:
    if number2 <= number1 and number2 <= number3 and number2 <= number4:
        print(number2)
    else:
        if number3 <= number2 and number3 <= number1 and number3 <= number4:
            print(number3)
        else:
            print(number4)

# modified
# print(min(int(input()), int(input()), int(input()), int(input())))
