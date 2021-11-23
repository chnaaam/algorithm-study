N, M = [int(n) for n in input().split(" ")]

not_hearing = {}
result = []

for _ in range(N):
    not_hearing.setdefault(input(), "")

for _ in range(M):
    text = input()

    if text in not_hearing:
        result.append(text)

result.sort()
print(len(result))

for r in result:
    print(r)
