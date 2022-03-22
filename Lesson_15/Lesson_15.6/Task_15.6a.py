def pos_to_dec(text, base):
    letters = 'ABCDEF'
    number = 0
    for i in range(len(text)):
        if text[i] in letters:
            number += (letters.find(text[i]) + 10) * base ** (len(text) - 1 - i)
        else:
            number += int(text[i]) * base ** (len(text) - 1 - i)
    return number


def dec_to_pos(number, base):
    result, n = '', number
    letters = 'ABCDEF'
    if n < base:
        if n > 9:
            return letters[n - 10]
        return n

    while True:
        if n // base > 0:
            if n % base > 9:
                result += letters[(n % base) - 10]
            else:
                result += str(n % base)
            n = n // base
        else:
            result += str(n % base)
            break
    return result[::-1]


number = int(input())
print(dec_to_pos(number, 2))
print(dec_to_pos(number, 8))
print(dec_to_pos(number, 16))
