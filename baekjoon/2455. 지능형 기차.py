max_people = -1
current_people_num = 0

for _ in range(4):
    o, i = [int(n) for n in input().split(" ")]

    current_people_num = current_people_num + i - o

    if max_people < current_people_num:
        max_people = current_people_num

print(max_people)