N = int(input())
text = []
for _ in range(N):
    text.append(input())

text_dict = {}
for t in list(set(text)):
    if len(t) not in text_dict:
        text_dict[len(t)] = []

    text_dict[len(t)].append(t)

sorted_text_keys = (sorted(text_dict.keys()))

for keys in sorted_text_keys:
    for value in sorted(text_dict[keys]):
        print(value)