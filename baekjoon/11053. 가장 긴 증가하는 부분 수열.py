# 시간 복잡도: O(n^2)

N = int(input())
arr = [int(n) for n in input().split(" ")]

M = [1] * (N + 1)

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            M[i] = max(M[i], M[j] + 1)

print(max(M))