N, K = [int(n) for n in input().split(" ")]
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0
for coin in coins:
    count += K // coin
    K = K % coin

print(count)