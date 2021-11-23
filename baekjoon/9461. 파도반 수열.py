T = int(input())

for _ in range(T):
    N = int(input())

    m = [0, 1, 1, 1, 2, 2] * (95)

    if N <= 5:
        print(m[N])
    else:
        for i in range(5, N + 1):
            m[i] = m[i - 1] + m[i - 5]

        print(m[N])
