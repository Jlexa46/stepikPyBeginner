def language_alphabet(text):
    uppercase_alphabet_en = [chr(i) for i in range(65, 90)]
    lowercase_alphabet_en = [chr(i) for i in range(97, 123)]
    uppercase_alphabet_ru = [chr(i) for i in range(1040, 1072)]
    lowercase_alphabet_ru = [chr(i) for i in range(1072, 1104)]

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
                index = uppercase_alphabet.index(c)
                if (index + shake_number) < alphabet_len:
                    cypher += uppercase_alphabet[index + shake_number]
                else:
                    cypher += uppercase_alphabet[index + shake_number - alphabet_len]
            else:
                index = lowercase_alphabet.index(c)
                if (index + shake_number) < alphabet_len:
                    cypher += lowercase_alphabet[index + shake_number]
                else:
                    cypher += lowercase_alphabet[index + shake_number - alphabet_len]
        else:
            cypher += c

    return cypher


sample = 'Блажен, кто верует, тепло ему на свете!'
sample2 = "To be, or not to be, that is the question!"
sample3 = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
sample4 = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
sample5 = "Hawnj pk swhg xabkna ukq nqj."
print(cezar_cypher(sample, 10))
print(cezar_cypher(sample2, 17))
print(cezar_cypher(sample3, -7))
print(cezar_cypher(sample4, 1))
print(cezar_cypher(sample5, 4))
