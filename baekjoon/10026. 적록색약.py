from collections import deque

N = 5#input()
inputs = [
    "RRRBB",
    "GGBBB",
    "BBBRR",
    "BBRRR",
    "RRRRR"
]

map = []
for i in inputs:
    map.append([c for c in list(i)])

non_b_map = []
for m in map:
    b_m = []
    for x in m:
        if x == "G":
            b_m.append("R")
        else:
            b_m.append(x)
    non_b_map.append(b_m)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(type, x, y):
    q = deque([(x, y)])
    count = 1

    while q:
        x, y = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < N and 0 <= ny < N:
                if map[ny][nx] == type:
                    q.append((nx, ny))
                    count += 1
                    map[ny][nx] = 0

    return count


def bfs2(type, x, y):
    q = deque([(x, y)])
    count = 1

    while q:
        x, y = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < N and 0 <= ny < N:
                if non_b_map[ny][nx] == type:
                    q.append((nx, ny))
                    count += 1
                    non_b_map[ny][nx] = 0

    return count

count = 0
for y in range(N):
    for x in range(N):
        if map[y][x] != 0:
            bfs(map[y][x], x, y)
            count += 1

n_count = 0
for y in range(N):
    for x in range(N):
        if non_b_map[y][x] != 0:
            bfs2(non_b_map[y][x], x, y)
            n_count += 1

print(count, n_count)