total_coins, count = 0, int(input())
while count != 0:
    if count >= 25:
        coins = count // 25
        total_coins += coins
        count -= coins * 25
    if count >= 10:
        coins = count // 10
        total_coins += coins
        count -= coins * 10
    if count >= 5:
        coins = count // 5
        total_coins += coins
        count -= coins * 5
    if count >= 1:
        coins = count // 1
        total_coins += coins
        count -= coins * 1
print(total_coins)

# modified
# count = int(input())
# print(count // 25 + count % 25 // 10 + count % 25 % 10 // 5 + count % 5)
