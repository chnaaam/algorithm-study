N = [int(c) for c in list(input())]
N.sort(reverse=True)
for n in N:
    print(n, end="")