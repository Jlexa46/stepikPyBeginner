number = int(input())
print('YES' if (999 < number <= 9999) and ((number % 7 == 0) or (number % 17 == 0)) else 'NO')
