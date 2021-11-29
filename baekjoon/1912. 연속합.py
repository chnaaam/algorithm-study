N = int(input())
arr = [int(n) for n in input().split(" ")]

m = [0] * 100001
m[0] = arr[0]

for i in range(1, len(arr)):
    m[i] = max(m[i - 1] + arr[i], arr[i])

print(max(m[:N]))