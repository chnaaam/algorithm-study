map = [
    [11, 12, 2, 24, 10],
    [16, 1, 13, 3, 25],
    [6, 20, 5, 21, 17],
    [19, 4, 8, 14, 9],
    [22, 15, 7, 23, 18]
]

numbers = [
    5, 10, 7, 16, 2,
    4, 22, 8, 17, 13,
    3, 18, 1, 6, 25,
    12, 19, 23, 14, 21,
    11, 24, 9, 20, 15
]

def search_xy(num):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == num:
                return (x, y)

    return (-1, -1)

def is_finished():
    # Vertical
    count = 0
    for i in range(5):
        if sum(map[:, i]) == 0:
            count += 1

    for i in range(5):
        if sum(map[i, :]) == 0:
            count += 1

for num in numbers:
    x, y = search_xy(num)

    map[y][x] = 0
