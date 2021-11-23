def is_prime_number(N):
    if N == 1:
        return False

    squared_n = int(N ** 0.5)

    for i in range(2, squared_n + 1):
        if N % i == 0:
            return False

    return True

count = 0
N = int(input())
for n in [int(n) for n in input().split(" ")]:
    if is_prime_number(n):
        count += 1

print(count)