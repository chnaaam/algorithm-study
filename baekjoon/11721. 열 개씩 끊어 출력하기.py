text = input()

i = 0
while True:
    if len(text) > 10:
        print(text[i * 10 : (i + 1) * 10])
        text = text[(i + 1) * 10 : ]
    else:
        print(text[i * 10: ])
        break
