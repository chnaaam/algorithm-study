N = int(input())

for _ in range(N):
    text = input()
    text = list(text)
    text[0] = text[0].upper()
    text = "".join(text)
    print(text)
