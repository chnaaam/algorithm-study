text_list = []

for _ in range(5):
    text_list.append(input())

vertical_idx = 0
len_text_list = text_list_count = len(text_list)
max_idx = max(text_list, key=len)

while True:
    if text_list_count == 0:
        break

    idx = vertical_idx % len_text_list

    if text_list[idx]:
        print(text_list[idx][0], end="")
        text_list[idx] = text_list[idx][1:]

        if not text_list[idx]:
            text_list_count -= 1


    vertical_idx += 1