N = int(input())

for i in range(N):
    for j in range(1, N - i):
        print(" ", end="")

    for j in range(i * 2 + 1):
        print("*", end="")

    print()