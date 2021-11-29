# Prefix Sum 배열을 배운 후에 참고

import sys

N, M = [int(n) for n in sys.stdin.readline().split(" ")]
arr = [int(n) for n in sys.stdin.readline().split(" ")]

for _ in range(M):
    s, e = [int(n) for n in sys.stdin.readline().split(" ")]

    print(sum(arr[s - 1 : e]))