A, B, C = [int(input()) for _ in range(3)]
num_dict = {i: 0 for i in range(10)}

for i in str(A * B * C):
    num_dict[int(i)] += 1

for i in range(10):
    print(num_dict[i])