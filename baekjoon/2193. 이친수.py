# 그래프로 그려보면 피보나치 수열과 동일한 식이 나옴

N = int(input())
m = [0] * 90
m[0] = 1
m[1] = 1

for i in range(2, N):
    m[i] = m[i - 1] + m[i - 2]

print(m[N - 1])
