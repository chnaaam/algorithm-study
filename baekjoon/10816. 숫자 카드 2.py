from collections import defaultdict

N = int(input())
arr = [int(n) for n in input().split(" ")]
K_num = int(input())
K_list = [int(n) for n in input().split(" ")]
num_dict = defaultdict(int)

for K in K_list:
    num_dict[K] = 0

for num in arr:
    num_dict[num] += 1

for K in K_list:
    if K in num_dict:
        print(num_dict[K], end=" ")
    else:
        print(0, end=" ")