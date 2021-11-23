from collections import deque

N, M = [int(n) for n in input().split(" ")]
map = []

for i in range(N):
    map.append([int(n) for n in list(input())])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = i + _dx, j + _dy

            if 0 <= nx < M and 0 <= ny < N:
                if map[ny][nx] == 1:
                    q.append((nx, ny))

                    # 핵심 코드
                    map[ny][nx] = map[j][i] + 1

    return map[N - 1][M - 1]

print(bfs(0, 0))
