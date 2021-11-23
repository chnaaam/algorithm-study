N = int(input())
stairs = []

for _ in range(N):
    stairs.append(int(input()))

m = [0] * N

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
elif N == 3:
    print(max(stairs[0], stairs[1]) + stairs[2])
else:
    m[0] = stairs[0]
    m[1] = stairs[0] + stairs[1]
    m[2] = max(stairs[1] + stairs[2], m[0] + stairs[2])

    for i in range(3, N):
        m[i] = max(m[i - 3] + stairs[i - 1] + stairs[i], m[i - 2] + stairs[i])

    print(m[N - 1])