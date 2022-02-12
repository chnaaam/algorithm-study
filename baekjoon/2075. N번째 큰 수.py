import heapq

data = []
N = int(input())

for _ in range(N):
    for num in [int(n) for n in input().split(" ")]:
        
        if len(data) < N:
            heapq.heappush(data, num)
        else:
            if data[0] < num:
                heapq.heappop(data)
                heapq.heappush(data, num)
                
print(data[0])