s = input()
print(s[:s.find('h') + 1] + s[s.rfind('h') - 1:s.find('h'):-1] + s[s.rfind('h'):])
