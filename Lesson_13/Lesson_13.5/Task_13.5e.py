# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        if word1 == word2:
            return False
        is_one_symble_different = False
        for i in range(len(word1)):
                if word1[:i] + word1[i+1:] == word2[:i] + word2[i+1:]:
                    is_one_symble_different = True
                    return is_one_symble_different
        return is_one_symble_different
    else:
        return False

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
