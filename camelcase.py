s = raw_input().strip()
words = 1
current_char = ""
for x in range(len(s)):
    if s[x].isupper():
        words += 1
print words
