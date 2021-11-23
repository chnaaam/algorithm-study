text = input()

suffixes = []
for i in range(len(text)):
    suffixes.append(text[i:])

suffixes.sort()

for s in suffixes:
    print(s)