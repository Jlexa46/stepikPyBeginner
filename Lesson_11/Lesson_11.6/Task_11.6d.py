for _ in range(int(input()[1:])):
    s = input()
    if s.count('#') > 0:
        s = s[:s.find('#')].rstrip()
    print(s)
