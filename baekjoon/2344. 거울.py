from collections import defaultdict


# N, M = 2, 3
# map = [
#     [0, 1, 0],
#     [0, 1, 1],
# ]

N, M = [int(n) for n in input().split(" ")]
map = []
for _ in range(N):
    map.append([int(n) for n in input().split(" ")])

# left -> right
# bottom -> top
# right -> left
# top -> bottom

lr_dir = True   # Left -> Right Direction
bt_dir = True   # Bottom -> Top Direction

points = defaultdict(dict)
point_idx = 1

for _ in range(2):
    if lr_dir:
        for i in range(N):
            points[point_idx] = {"x": -1, "y": i, "dir": "right"}
            point_idx += 1
    else:
        for i in range(N - 1, -1, -1):
            points[point_idx] = {"x": M, "y": i, "dir": "left"}
            point_idx += 1

    lr_dir = False

    if bt_dir:
        for i in range(M):
            points[point_idx] = {"x": i, "y": N, "dir": "top"}
            point_idx += 1
    else:
        for i in range(M - 1, -1, -1):
            points[point_idx] = {"x": i, "y": -1, "dir": "bottom"}
            point_idx += 1

    bt_dir = False

DIRECTION = {
    "left": (-1, 0),
    "right": (1, 0),
    "top": (0, -1),
    "bottom": (0, 1),
}

def is_finished(x, y):
    if not(0 <= x < M and 0 <= y < N):
        return True

    return False

def change_current_dir(current_dir):
    if current_dir == "right":
        current_dir = "top"
    elif current_dir == "left":
        current_dir = "bottom"
    elif current_dir == "top":
        current_dir = "right"
    else: # Bottom
        current_dir = "left"

    return current_dir

def get_position(x, y):
    for key, value in points.items():
        if value["x"] == x and value["y"] == y:
            return key

    return -1

for key, value in points.items():
    cx, cy, current_dir = value["x"], value["y"], value["dir"]

    dx, dy = DIRECTION[current_dir]

    cx += dx
    cy += dy

    while not is_finished(cx, cy):
        if map[cy][cx] == 1:
            current_dir = change_current_dir(current_dir)

        dx, dy = DIRECTION[current_dir]

        cx += dx
        cy += dy

    print(get_position(cx, cy), end=" ")