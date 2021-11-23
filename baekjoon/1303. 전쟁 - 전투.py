from collections import deque

N, M = [int(n) for n in input().split(" ")]
map = []
for _ in range(M):
    map.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(type, x, y):
    q = deque([(x, y)])
    map[y][x] = 0
    idx = 1

    while q:
        x, y = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < N and 0 <= ny < M:
                if map[ny][nx] == type:
                    q.append((nx, ny))
                    map[ny][nx] = idx
                    idx += 1

    return idx ** 2

count_w = 0
count_b = 0

for y in range(M):
    for x in range(N):
        if map[y][x] == "W":
            count_w += bfs("W", x, y)
        elif map[y][x] == "B":
            count_b += bfs("B", x, y)

print(count_w, count_b)