N = int(input())

for _ in range(N):
    buffer = input().split()

    iter_num, text = int(buffer[0]), buffer[1]

    result = ""
    for t in text:
        result += t * iter_num

    print(result)