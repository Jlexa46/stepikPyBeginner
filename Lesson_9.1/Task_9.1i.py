s, total = input(), 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        total += 1
print(total)
