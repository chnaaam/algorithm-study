def sum123(n):
    m = [0] * (n + 1)

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        m[1], m[2], m[3] = 1, 2, 4

        for i in range(4, n + 1):
            m[i] = m[i - 1] + m[i - 2] + m[i - 3]

        return m[n]

N = int(input())
for _ in range(N):
    print(sum123(int(input())))