# Out of memory

import heapq

N = int(input())
k = int(input())

B = []
for i in range(N):
    for j in range(N):
        n = (-1) * (i + 1) * (j + 1)
        
        if len(B) < k:
            heapq.heappush(B, n)
        else:
            if B[0] < n:
                heapq.heappop(B)
                heapq.heappush(B, n)
        
print((-1) * B[0])