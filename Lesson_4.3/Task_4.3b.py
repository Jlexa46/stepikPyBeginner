a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

# modified
# a, b, c = int(input()), int(input()), int(input())
# print('Равносторонний' if a == b == c else 'Равнобедренный' if a == b or b == c or a == c else 'Разносторонний')
