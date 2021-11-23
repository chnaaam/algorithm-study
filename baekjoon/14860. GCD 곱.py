def gcd(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b

    return abs(b)

N, M = [int(n) for n in input().split(" ")]
answer = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        answer *= gcd(i, j)

print(answer)