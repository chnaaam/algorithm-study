from collections import deque

text = input()
sub_text = input()
sub_text_dict = {}

text_q = deque(list(text))

for t in sub_text:
    if t not in sub_text_dict:
        sub_text_dict.setdefault(t, "")

res = ""
while text_q:
    t = text_q.popleft()

    if t not in sub_text_dict:
        res += t

if res:
    print(res)
else:
    print("FRULA")