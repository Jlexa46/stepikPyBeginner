shake = int(input())
for c in input():
    char = ord(c) - shake
    if (ord(c) - shake) < 96:
        char += 26
    print(chr(char), end='')
