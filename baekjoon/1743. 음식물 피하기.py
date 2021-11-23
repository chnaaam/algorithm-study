from collections import deque


N, M, K = [int(n) for n in input().split(" ")]
inputs = []
for _ in range(K):
    inputs.append([int(n) for n in input().split(" ")])

map = [[0] * (M + 1) for _ in range(N + 1)]

for y, x in inputs:
    map[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    map[y][x] = 0
    idx = 1

    while q:
        x, y = q.popleft()
        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < M + 1 and 0 <= ny < N + 1:
                if map[ny][nx] == 1:
                    q.append((nx, ny))
                    map[ny][nx] = 0
                    idx += 1

    return idx

max_value = -1

for y in range(1, N + 1):
    for x in range(1, M + 1):
        if map[y][x] == 1:
            value = bfs(x, y)

            if max_value < value:
                max_value = value

print(max_value)