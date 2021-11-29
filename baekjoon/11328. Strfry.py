from collections import defaultdict


N = int(input())

for _ in range(N):
    A, B = input().split(" ")

    A_set = defaultdict(int)
    for c in A:
        A_set[c] += 1

    is_possible = True

    if len(A) != len(B):
        is_possible = False
    else:
        for b in B:
            if b not in A_set:
                is_possible = False
                break


            A_set[b] -= 1

            if A_set[b] < 0:
                is_possible = False
                break

    if is_possible:
        print("Possible")
    else:
        print("Impossible")