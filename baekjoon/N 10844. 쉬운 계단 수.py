# a[n] = 2 * a[n - 1] + 1

N = int(input())
m = [0] * (N + 1)
m[1] = 9

for i in range(2, N + 1):
    m[i] = 2 * m[i - 1] - 1

print(m[N] % 1000000000)