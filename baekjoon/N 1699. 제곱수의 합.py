while True:
    N = int(input())

    V = int(N ** 0.5)
    m = [0] * (V + 1)
    count = 0
    for i in range(V, 0, -1):
        if m[i] == 0:
            m[i] = i * i

        while N - m[i] >= 0:
            N = N - m[i]
            count += 1

    print(count)
