import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    CMD = sys.stdin.readline().replace("\n", "")
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().replace("\n", "")

    if N == 0:
        arr = []
    else:
        arr = [int(n) for n in arr[1:-1].split(",")]
    arr = deque(arr)
    is_error = False
    is_reversed = False

    for c in CMD:
        if c == "R":
            is_reversed = not is_reversed
        elif c == "D":
            if arr:
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                is_error = True
                break

    if not is_error:
        if is_reversed:
            arr.reverse()

        print(f"[{','.join([str(n) for n in list(arr)])}]", sep="")
    else:
        print("error")