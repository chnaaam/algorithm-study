M, N = [int(n) for n in input().split(" ")]

# 에라토스테네스의 체
# num에 대해 모두 소수를 구하지 않고, square(num)까지만 확인해도 된다.
def is_prime_number(num):
    squared_num = int(num ** 0.5) + 1

    for i in range(2, squared_num):
        if num % i == 0:
            return False

    return True

for i in range(M, N + 1):
    if i < 2:
        continue

    if is_prime_number(i):
        print(i)