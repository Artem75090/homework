def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().count(root_word.lower()) >= 1 or root_word.lower().count(i.lower()) >= 1:
            same_words.append(i)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))