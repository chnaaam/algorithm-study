"""
bfs 방식으로 체크해가면서 방문한 곳은 0으로 체크한다.
"""
from collections import deque


dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

while True:
    W, H = [int(n) for n in input().split(" ")]

    if W == 0 and H == 0:
        break

    map = []
    for _ in range(H):
        map.append([int(n) for n in input().split(" ")])


    def bfs(x, y):
        q = deque([(x, y)])
        map[y][x] = 0

        while q:
            x, y = q.popleft()

            for _dx, _dy in zip(dx, dy):
                nx, ny = x + _dx, y + _dy

                if 0 <= nx < W and 0 <= ny < H:
                    if map[ny][nx] == 1:
                        q.append((nx, ny))
                        map[ny][nx] = 0

    count = 0
    for y in range(H):
        for x in range(W):
            if map[y][x] == 1:
                bfs(x, y)
                count += 1

    print(count)