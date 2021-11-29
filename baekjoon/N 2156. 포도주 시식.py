N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
m = [0] * 10001

m[1] = arr[1]
m[2] = m[1] + arr[2]

for i in range(3, len(arr)):
    # i = i - 1

    m[i] = max(m[i - 2] + arr[i], m[i - 3] + arr[i - 1] + arr[i])

print(m[N - 1])