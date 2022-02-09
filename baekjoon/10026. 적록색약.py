from collections import deque

N = int(input())
inputs = []
for _ in range(N):
    inputs.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
VISITED = "-"

def get_region(isIngoreR):
    map = []
    for inp in inputs:
        m = []
        for i in inp:
            if isIngoreR:
                if i == "R":
                    m.append("G")
                else:
                    m.append(i)
            else:
                m.append(i)
        map.append(m)

    def bfs(type, x, y):
        q = deque([(x, y)])
        map[y][x] = VISITED
        count = 1

        while q:
            x, y = q.popleft()

            for _dx, _dy in zip(dx, dy):
                nx, ny = x + _dx, y + _dy

                if 0 <= nx < N and 0 <= ny < N:
                    if map[ny][nx] == type:
                        q.append((nx, ny))
                        map[ny][nx] = VISITED

        return count

    count = 0
    for y in range(N):
        for x in range(N):
            if map[y][x] != VISITED:
                bfs(map[y][x], x, y)
                count += 1
                
    return count

print(get_region(False), get_region(True))

