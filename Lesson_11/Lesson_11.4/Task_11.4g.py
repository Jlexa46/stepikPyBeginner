list = []
for _ in range(int(input())):
    list.append(int(input()))
negatives = zeros = positives = ''
for el in list:
    if el < 0:
        negatives += str(el) + '\n'
    elif el == 0:
        zeros += str(el) + '\n'
    else:
        positives += str(el) + '\n'
print(negatives + zeros + positives)
