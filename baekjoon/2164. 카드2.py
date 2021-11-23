from collections import deque


N = int(input())
q = deque([n + 1 for n in range(N)])

if len(q) == 1:
    print(q.popleft())
else:
    while True:
        _ = q.popleft()

        if len(q) == 1:
            break

        item = q.popleft()
        q.append(item)

    print(q.popleft())