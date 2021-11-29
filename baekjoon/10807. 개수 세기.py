N = int(input())
arr = [int(n) for n in input().split(" ")]

V = int(input())
count = 0

for num in arr:
    if V == num:
        count += 1

print(count)