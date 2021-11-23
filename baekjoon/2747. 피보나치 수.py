m = [0] * 46
m[0] = 0
m[1] = 1
m[2] = 1

def fibonacci(n):
    if n == 0 or n == 1 or n == 2:
        return m[n]

    if m[n] == 0:
        m[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return m[n]

print(fibonacci(int(input())))