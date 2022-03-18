numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(*numbers, sep='\n')
