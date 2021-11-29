# 미리 주어진 범위만큼 에라토스테네스의 체를 계산
# 리스트에 데이터가 있는지 확인하는 건 O(n)이기 때문에 다른 방법을 사용
# Set은 순서가 없기 때문에 Dictionary를 이용해서 풀었음

def is_prime_number(num):
    sqrt_num = int(num ** 0.5) + 1
    for i in range(2, sqrt_num):
        if num % i == 0:
            return False

    return True

prime_number_list = {}
for i in range(2, 10001):
    if is_prime_number(i):
        prime_number_list.setdefault(i, 0)

# prime_number_list = OrderedDict(prime_number_list)

N = int(input())

for _ in range(N):
    num = int(input())

    min_prime_dist = 10000
    prime_num1 = -1
    prime_num2 = -1

    for prime_num in prime_number_list:
        if num < prime_num:
            break

        if num - prime_num in prime_number_list:
            if abs(num - prime_num - prime_num) < min_prime_dist:
                min_prime_dist = abs(num - prime_num - prime_num)

                if prime_num < num - prime_num:
                    prime_num1 = prime_num
                    prime_num2 = num - prime_num
                else:
                    prime_num1 = num - prime_num
                    prime_num2 = prime_num

    print(f"{prime_num1} {prime_num2}")
