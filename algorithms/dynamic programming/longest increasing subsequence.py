arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

M = [1] * (len(arr) + 1)

for i in range(1, len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            M[i] = max(M[i], M[j] + 1)

print(max(M))