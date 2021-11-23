K = int(input())
if K == 1:
    print(0, 1)
else:
    m = [0] * (K + 1)
    m[0] = 1
    m[1] = 1

    for i in range(2, K + 1):
        m[i] = m[i - 1] + m[i - 2]

    print(m[K - 2], m[K - 1])