N = int(input())


def get_decompose_number(num):
    res = num

    while num:
        res += num % 10
        num = num // 10

    return res


min_num = N + 1
for i in range(N):
    decomposed_number = get_decompose_number(i)

    if decomposed_number == N:
        if min_num > i:
            min_num = i

if min_num == N + 1:
    print(0)
else:
    print(min_num)


