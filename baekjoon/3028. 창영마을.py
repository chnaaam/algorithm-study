seq = input()
arr = [1, 0, 0]


for s in seq:
    if s == "A":
        arr[0], arr[1] = arr[1], arr[0]
    elif s == "B":
        arr[1], arr[2] = arr[2], arr[1]
    else:
        arr[0], arr[2] = arr[2], arr[0]

answer = -1
for i in range(len(arr)):
    if arr[i] == 1:
        answer = i
        break

print(answer + 1)