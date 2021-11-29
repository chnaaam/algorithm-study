from collections import deque


N, K = [int(n) for n in input().split(" ")]
arr = deque([i + 1 for i in range(N)])
idx = 1
res = []
while arr:
    value = arr.popleft()
    if idx % K == 0:
        res.append(value)
    else:
        arr.append(value)

    idx += 1

print(f"<{', '.join([str(i) for i in res])}>")

