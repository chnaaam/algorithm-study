def tiling(n):
    m = [0] * (n + 1)

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        m[1], m[2] = 1, 2

        for i in range(3, n + 1):
             m[i] =  m[i - 1] + m[i - 2]

        return m[n]

N = int(input())
print(tiling(N) % 10007)