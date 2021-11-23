import sys

N = int(input())

for _ in range(N):
    a, b = [int(n) for n in sys.stdin.readline().strip().split(" ")]
    print(a + b)