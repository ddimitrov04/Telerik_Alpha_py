def special_word(words):
    read = {}
    for word in words:
        special = ''.join(sorted(word))
        if special not in read:
            read[special] = word

    return list(read.values())

words = input().split()
new_words = special_word(words)
print(*new_words)
