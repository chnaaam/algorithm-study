count = 0
for i in range(8):
    text = input()

    for j in range(len(text)):
        if (i + j) % 2 == 0:
            if text[j] == "F":
                count += 1

print(count)