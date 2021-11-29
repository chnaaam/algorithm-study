from collections import deque

N, K = [int(n) for n in input().split(" ")]
q = deque([i + 1 for i in range(N)])

count = 0
res = []

while q:
    n = q.popleft()
    count += 1

    if K == count:
        count = 0
        res.append(n)
    else:

        q.append(n)



print(f"<{', '.join([str(n) for n in res])}>")