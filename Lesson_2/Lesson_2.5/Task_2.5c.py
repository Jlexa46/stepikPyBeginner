n, k = int(input()), int(input())
print(k // n, k % n, sep='\n')

# modified
# print(*(lambda n,k: (k // n, k % n))(int(input()), int(input())), sep='\n')
