def is_prime_number(N):
    if N == 1:
        return False

    squared_n = int(N ** 0.5)

    for i in range(2, squared_n + 1):
        if N % i == 0:
            return False

    return True

M = int(input())
N = int(input())
prime_numbers = []
for n in [i for i in range(M, N + 1)]:
    if is_prime_number(n):
        prime_numbers.append(n)

if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)