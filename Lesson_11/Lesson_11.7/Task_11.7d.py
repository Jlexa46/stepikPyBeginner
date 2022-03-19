palindromes = [num for num in range(100, 1000) if str(num) == str(num)[::-1]]
print(palindromes)
