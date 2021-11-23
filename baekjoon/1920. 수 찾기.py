N = int(input())
arr = [int(n) for n in input().split(" ")]
K_num = int(input())
K_list = [int(n) for n in input().split(" ")]

arr.sort()

def sort(arr, N, K):
    left, right = 0, N - 1

    while left <= right:
        middle = left + (right - left) // 2

        if arr[middle] == K:
            return 1

        elif arr[middle] < K:
            left = middle + 1

        else:
            right = middle - 1

    return 0

for K in K_list:
    print(sort(arr, N, K))