N, K = [int(n) for n in input().split(" ")]

# 재귀로 구현 -> RecursionError
def factorial_recur(n):
    if n == 1:
        return 1

    return n * factorial_recur(n - 1)

# 반복문으로 구현
def factorial_iter(n):
    result = 1

    for i in range(n, 0, -1):
        result *= i

    return result

print(factorial_iter(N) // (factorial_iter(K) * (factorial_iter(N - K))))