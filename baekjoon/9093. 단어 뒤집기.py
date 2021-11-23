N = int(input())

for _ in range(N):
    for text in input().split(" "):
        print(text[::-1], end=" ")
    print()