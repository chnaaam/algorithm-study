text = input()
alpa_dict = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

for c in text:
    alpa_dict[c] += 1

for key in alpa_dict.keys():
    print(alpa_dict[key], end=" ")