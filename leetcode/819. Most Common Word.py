from collections import defaultdict

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]

paragraph = paragraph.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")
words = paragraph.split(" ")

counted_words = defaultdict(int)

for word in words:
    if word:
        if word.lower() not in banned:
            counted_words[word.lower()] += 1

sorted_counted_words = sorted(counted_words.items(), key=lambda x: x[1], reverse=True)

most_freq_word = sorted_counted_words[0]

print(most_freq_word[0])
