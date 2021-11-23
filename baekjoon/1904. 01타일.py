# 점화식: a[i] = a[i - 1] + a[i - 2]

N = int(input())

m = [0] * (N)

m[0] = 1

if N > 1:
    m[1] = 2

    for i in range(2, N):
        m[i] = (m[i - 1] + m[i - 2]) % 15746

print(m[N - 1])