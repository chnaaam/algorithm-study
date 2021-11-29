from collections import deque

N = int(input())
K = int(input())
map = [[0] * N for _ in range(N)]

map[0][0] = 2

for _ in range(K):
    y, x = [int(n) for n in input().split(" ")]
    map[y - 1][x - 1] = 1

L = int(input())
steps = deque()
for _ in range(L):
    step, dir = input().split(" ")
    steps.append((int(step), dir))

prev_sec = 0
dir_idx = 0
current_pos = {"x": 0, "y": 0}
current_sec = 0
snake = deque([(0, 0)])

DIR_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_finished(x, y):
    if not(0 <= x < N and 0 <= y < N):
        return True

    for sx, sy in snake:
        if sx == x and sy == y:
            return True

    return False


def switch_dir(dir, dir_idx):
    if dir == "D":
        dir_idx += 1

        if dir_idx >= len(DIR_LIST):
            dir_idx = 0

    elif dir == "L":
        dir_idx -= 1

        if dir_idx < 0:
            dir_idx = len(DIR_LIST) - 1

    return dir_idx


while True:
    if steps:
        sec, dir = steps.popleft()
        sec -= prev_sec

    else:
        # step이 없는 경우 맵 밖으로 나가게 하기 위해
        sec = N + 1

    finish = False

    for _ in range(sec):
        current_sec += 1

        x, y = snake[-1]

        dx, dy = DIR_LIST[dir_idx]
        nx = x + dx
        ny = y + dy

        if is_finished(nx, ny):
            finish = True
            break

        if map[ny][nx] == 1:
            K -= 1
        else:
            x, y = snake.popleft()
            map[y][x] = 0

        snake.append((nx, ny))
        map[ny][nx] = 2

    if finish:
        break

    dir_idx = switch_dir(dir, dir_idx)
    prev_sec = sec + prev_sec

print(current_sec)