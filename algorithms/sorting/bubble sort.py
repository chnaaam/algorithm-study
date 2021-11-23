N = 5
num_list = [7, 4, 5, 1, 3]

for i in range(N):
    for j in range(i + 1, N):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print(num_list)