from collections import deque

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

LAND = "1"
WATER = "0"
VISITED_TAG = "2"

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

island_num = 0

len_y = len(grid)
len_x = len(grid[0])

for i in range(len_y):
    for j in range(len_x):
        
        if grid[i][j] == LAND:
            island_num += 1
            q = deque([[j, i]])

            while q:
                x, y = q.popleft()

                grid[y][x] = VISITED_TAG

                for dx, dy in zip(DX, DY):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len_x and 0 <= ny < len_y:
                        if grid[ny][nx] == LAND:
                            q.append([nx, ny])

            
            
            
print(island_num)