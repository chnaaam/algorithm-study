text = input()

num_pad = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
answer = 0

for t in list(text):
    for idx, num in enumerate(num_pad):
        if t in num:
            answer += idx + 3
            break

print(answer)
