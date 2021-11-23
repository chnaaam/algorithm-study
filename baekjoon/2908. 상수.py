A, B = [n for n in input().split(" ")]

print(max([int(A[::-1]), int(B[::-1])]))