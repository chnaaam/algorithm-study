from collections import defaultdict

N = int(input())
text_dict = defaultdict(int)

for _ in range(N):
    text = input()

    text_dict[text] += 1

res = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)
text_list = [res[0][0]]
max_count = res[0][1]

for text, count in res[1:]:
    if max_count == count:
        text_list.append(text)
    else:
        break

text_list.sort()
print(text_list[0])