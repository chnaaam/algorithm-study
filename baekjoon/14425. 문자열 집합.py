N, M = [int(n) for n in input().split(" ")]

text_set = set()
text_list = []

for _ in range(N):
    text_set.add(input())

count = 0
for _ in range(M):
    text_list.append(input())

for text in text_list:
    if text in text_set:
        count += 1

print(count)