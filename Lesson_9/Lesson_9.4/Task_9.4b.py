dna = input().lower()
counter_a = counter_g = counter_c = counter_t = 0
for c in dna:
    if c == 'а':
        counter_a += 1
    if c == 'г':
        counter_g += 1
    if c == 'ц':
        counter_c += 1
    if c == 'т':
        counter_t += 1
print('Аденин: ', counter_a,
      '\nГуанин: ', counter_g,
      '\nЦитозин: ', counter_c,
      '\nТимин: ', counter_t, sep='')
