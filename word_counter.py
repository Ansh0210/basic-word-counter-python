sample_text = """Hello Hello bye  hi hi"""

word_count = {}

for word in sample_text.lower().split():
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
