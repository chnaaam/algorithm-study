from collections import deque


M, N = [int(n) for n in input().split(" ")]
map = []
for _ in range(N):
    map.append([int(n) for n in input().split(" ")])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for y in range(N):
    for x in range(M):
        if map[y][x] == 1:
            q.append((x, y))

def bfs():
    max_idx = 0
    while q:
        x, y = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < M and 0 <= ny < N:
                if map[ny][nx] == 0:
                    q.append((nx, ny))
                    max_idx = map[ny][nx] = map[y][x] + 1

    return max_idx - 1

answer = bfs()

is_not_filled = False

for y in range(N):
    for x in range(M):
        if map[y][x] == 0:
            is_not_filled = True
            break

if not is_not_filled:
    if answer == -1:
        print(0)
    else:
        print(answer)
else:
    print(-1)



# if answer == -1:
#     print(0)
# else:
