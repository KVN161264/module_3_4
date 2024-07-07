def single_root_words(root_word, *other_words):
    same_words = []
    w_lower = root_word.lower()
    for i in other_words:
        other_w_lower = i.lower()
        if w_lower in other_w_lower or other_w_lower in w_lower:
            same_words.append(i)
    return same_words
print(single_root_words('care', 'Career', 'uncareful', 'carefully', 'carte'))
print(single_root_words('ball', 'basketball', 'balanse', 'Handball', 'balloon'))


