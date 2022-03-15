s, counter = input(), -2
for i in range(len(s)):
    if s[i] == 'f':
        counter += 1
    if counter == 0:
        print(i)
        break
else:
    print(counter)
