arr = [
    0, 1, 1, 2,
    3, 5, 8, 13,
    21, 34, 55, 89,
    144, 233, 377, 610
]
X = 610
N = len(arr)
M = int(N ** 0.5) + 1

def jump_sort(N, arr, X):
    step = M
    prev = 0

    # Jump Search
    while arr[int(min(step, N) - 1)] < X:
        prev = step
        step += M
        if prev >= N:
            return -1

    # Linear Search
    while arr[int(prev)] < X:
        prev += 1

        if prev == min(step, N):
            return -1

    if arr[int(prev)] == X:
        return prev

    return -1

print(jump_sort(N, arr, X))