T = int(input())

for _ in range(T):
    N = int(input())
    chars = input().split(" ")
    res = chars[0]

    for c in chars[1:]:
        if ord(res[0]) < ord(c):
            res += c
        else:
            res = c + res

    print(res)

