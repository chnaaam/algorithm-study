N = int(input())

for i in range(1, N):
    for j in range(N - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

for i in range(N):
    for j in range(i):
        print(" ", end="")

    for j in range(2 * (N - i) - 1):
        print("*", end="")

    print()