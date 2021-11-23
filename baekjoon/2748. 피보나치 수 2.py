N = int(input())

m = [0] * (N + 1)

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    m[0] = 0
    m[1] = 1
    for i in range(2, n + 1):
        m[i] = m[i - 1] + m[i - 2]

    return m[n]

print(fibonacci(N))