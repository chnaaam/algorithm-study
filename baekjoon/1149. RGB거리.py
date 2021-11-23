N = int(input())
home_rgb_list = []
for _ in range(N):
    home_rgb_list.append([int(n) for n in input().split(" ")])

rm = [0] * (N)
gm = [0] * (N)
bm = [0] * (N)

rm[0] = home_rgb_list[0][0]
gm[0] = home_rgb_list[0][1]
bm[0] = home_rgb_list[0][2]

for i in range(1, len(home_rgb_list)):
    r, g, b = home_rgb_list[i]

    rm[i] = min(gm[i - 1], bm[i - 1]) + r
    gm[i] = min(rm[i - 1], bm[i - 1]) + g
    bm[i] = min(rm[i - 1], gm[i - 1]) + b

print(min(rm[N - 1], gm[N - 1], bm[N - 1]))
