# # 1번 풀이
# def is_prime_number(num):
#     sqrt_num = int(num ** 0.5) + 1
#     for i in range(2, sqrt_num):
#         if num % i == 0:
#             return False
#
#     return True
#
# def prime_number_count(num):
#     count = 0
#     for i in range(num + 1, 2 * num + 1):
#         if is_prime_number(i):
#             count += 1
#             print(i)
#     return count
#
# while True:
#     N = int(input())
#
#     if N == 0:
#         break
#
#     print(prime_number_count(N))


# 2번 풀이
def is_prime_number(num):
    sqrt_num = int(num ** 0.5) + 1
    for i in range(2, sqrt_num):
        if num % i == 0:
            return False

    return True

prime_number_list = []
for i in range(1, 123456 * 2 + 1):
    if is_prime_number(i):
        prime_number_list.append(i)

while True:
    N = int(input())

    if N == 0:
        break

    count = 0
    for prime_num in prime_number_list:
        if N < prime_num <= 2 * N:
            count += 1

    print(count)
