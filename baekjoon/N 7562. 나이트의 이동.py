from collections import deque


UNVISITED = 0
VISITED = 1

N = int(input())

for _ in range(N):
    M = int(input())
    map = []
    for _ in range(M):
        map.append([UNVISITED for _ in range(M)])

    sx, sy = [int(n) for n in input().split(" ")]
    gx, gy = [int(n) for n in input().split(" ")]

    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    def bfs(x, y):
        q = deque([(x, y)])
        map[y][x] = 0

        while q:
            x, y = q.popleft()

            if x == gx and y == gy:
                break

            for _dx, _dy in zip(dx, dy):
                nx, ny = x + _dx, y + _dy

                if 0 <= nx < M and 0 <= ny < M:
                    if map[ny][nx] == UNVISITED:
                        q.append((nx, ny))
                        map[ny][nx] = map[y][x] + 1

        return map[gy][gx]

    print(bfs(sx, sy))