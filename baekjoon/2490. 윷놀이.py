for _ in range(3):
    buffer = [int(n) for n in input().split(" ")]

    count0 = 0
    count1 = 0
    for b in buffer:
        if b == 0:
            count0 += 1
        else:
            count1 += 1

    if count0 == 1:
        print("A")
    elif count0 == 2:
        print("B")
    elif count0 == 3:
        print("C")
    elif count0 == 4:
        print("D")
    else:
        print("E")