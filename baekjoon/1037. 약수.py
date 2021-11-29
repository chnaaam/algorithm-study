N = int(input())
num_list = [int(n) for n in input().split(" ")]

if len(num_list) == 1:
    print(num_list[0] ** 2)
else:
    num_list.sort()
    print(num_list[0] * num_list[-1])
