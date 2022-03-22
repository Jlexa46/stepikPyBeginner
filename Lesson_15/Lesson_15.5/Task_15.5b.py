def language_alphabet(text):
    uppercase_alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lowercase_alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    if 65 <= ord(text[0]) <= 123:
        return uppercase_alphabet_en, lowercase_alphabet_en, 26
    else:
        return uppercase_alphabet_ru, lowercase_alphabet_ru, 32


def cezar_cypher(text, shake_number):
    uppercase_alphabet, lowercase_alphabet, alphabet_len = language_alphabet(text)
    cypher = ''

    for c in text:
        if c.isalpha():
            if c.isupper():
                index = uppercase_alphabet.find(c)
                if (index + shake_number) < alphabet_len:
                    cypher += uppercase_alphabet[index + shake_number]
                else:
                    cypher += uppercase_alphabet[index + shake_number - alphabet_len]
            else:
                index = lowercase_alphabet.find(c)
                if (index + shake_number) < alphabet_len:
                    cypher += lowercase_alphabet[index + shake_number]
                else:
                    cypher += lowercase_alphabet[index + shake_number - alphabet_len]
        else:
            cypher += c

    return cypher


word = ''
s = ''
for c in input():
    if c.isalpha():
        word += c
    else:
        if len(word) > 0:
            s += cezar_cypher(word, len(word))
        word = ''
        s += c
if word !='':
    s += cezar_cypher(word, len(word))
print(s)

