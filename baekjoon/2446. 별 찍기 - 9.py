N = int(input())

for i in range(N - 1, 0, -1):
    for j in range(1, N - i):
        print(" ", end="")

    for j in range(i * 2 + 1):
        print("*", end="")

    print()

for i in range(N):
    for j in range(1, N - i):
        print(" ", end="")

    for j in range(i * 2 + 1):
        print("*", end="")

    print()