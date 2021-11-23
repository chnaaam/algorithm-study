while True:
    A, B = [int(n) for n in input().split(" ")]

    if A == 0 and B == 0:
        break

    print(A + B)