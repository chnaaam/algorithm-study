num_eng_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "none": "a"
}

M, N = [int(n) for n in input().split(" ")]

num_arr = []
for i in range(M, N + 1):
    if i < 10:
        num_arr.append((num_eng_dict[i], num_eng_dict["none"], i))
    else:
        A = i // 10
        B = i % 10

        num_arr.append((num_eng_dict[A], num_eng_dict[B], i))

num_arr.sort(key=lambda x: (x[0], x[1]))
for i, (_, _, num) in enumerate(num_arr):
    if i % 10 == 0 and i != 0:
        print()
    print(num, end=" ")
