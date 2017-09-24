def get_counts(word):
    counts = dict()
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts



def anagram(word1,word2):
    return get_counts(word1) == get_counts(word2)
