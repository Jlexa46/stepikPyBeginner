s = input()
most_popular, char = s.count(s[0]), s[0]
while s != '':
    c = s[-1]
    if most_popular < s.count(c):
        most_popular, char = s.count(c), c
    s = s[:len(s) - 1]
print(char)
