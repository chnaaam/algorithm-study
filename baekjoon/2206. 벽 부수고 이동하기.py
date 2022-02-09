"""
반례
7 4
0000
1110
0000
0111
0000
0011
0010
"""

from collections import deque

N, M = [int(n) for n in input().split(" ")]
inputs = []
for _ in range(N):
    inputs.append(input())

map = []
visited_map = []
for inp in inputs:
    map.append([int(i) for i in inp])
    visited_map.append([[0, 0] for i in inp])

PATH = 0
WALL = 1
VISITED = 2

DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([[x, y, 1]])
    visited_map[0][0][1] = 1
    
    while q:
        x, y, w = q.popleft()
        
        if x == M - 1 and y == N - 1:
            return visited_map[y][x][w]
        
        for dx, dy in zip(DX, DY):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N:
                if map[ny][nx] == WALL and w == 1:
                    visited_map[ny][nx][0] = visited_map[y][x][1] + 1
                    q.append([nx, ny, 0])
                elif map[ny][nx] == PATH and visited_map[ny][nx][w] == 0:
                    visited_map[ny][nx][w] = visited_map[y][x][w] + 1                
                    q.append([nx, ny, w])
                    
    return -1
    
print(bfs(0, 0))

