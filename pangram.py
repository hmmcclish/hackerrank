alphabet = set("abcdefghijklmnopqrstuvwxyz")
test_phrase = set(str(raw_input().strip(' ,. ').lower()))
if ' ' in test_phrase:
    test_phrase.remove(' ')
if alphabet == test_phrase:
    print "pangram"
else:
    print "not pangram"
