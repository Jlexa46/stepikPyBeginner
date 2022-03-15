s = input()
s = s[len(s) if len(s) // 2 == 0 else (len(s) + 1) // 2:] + s[:len(s) if len(s) // 2 == 0 else (len(s) + 1) // 2]
print(s)
