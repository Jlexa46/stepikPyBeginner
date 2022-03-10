sequence_1, sequence_2, n = 1, 0, int(input())
print('1', end=' ')
for _ in range(n - 1):
    sequence_1, sequence_2 = sequence_2 + sequence_1, sequence_1
    print(sequence_1, end=' ')
