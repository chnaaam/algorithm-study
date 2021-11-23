N = int(input())

for _ in range(N):
    print(sum([int(num) for num in input().split(",")]))