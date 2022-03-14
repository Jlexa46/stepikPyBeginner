count = 0
product = 1
for _ in range(10):
    x = int(input())
    if x >= 0:
        product *= x
        count += 1
if count > 0:
    print(count)
    print(product)
else:
    print('NO')
