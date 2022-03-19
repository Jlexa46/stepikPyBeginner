s = input().lower().split()
print('Общее количество артиклей:', s.count('a') + s.count('an') + s.count('the'))
