X = int(input())
m = [0] * (X + 1)

for i in range(2, X + 1):

    # 1로 빼는 경우
    m[i] = m[i - 1] + 1

    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        m[i] = min(m[i], m[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        m[i] = min(m[i], m[i // 3] + 1)

print(m[X])