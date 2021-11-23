for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = [int(n) for n in input().split(" ")]

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 1. 두 점이 일치하는 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    # 2. 두 점이 일치하지만 원 반지름이 다른 경우
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)

    # 3. 한 원이 다른 원을 포함하고 있지만 포함되는 원 반지름이 작은 경우
    elif distance ** 0.5 + r1 == r2 or distance ** 0.5 + r2 == r1:
        print(1)

    # 4. 원이 한 점에서 만나는 경우
    elif distance == (r1 + r2) ** 2:
        print(1)

    # 5. 원이 두 점에서 만나는 경우
    elif distance <  (r1 + r2) ** 2:
        print(2)

    # 6. 원이 만나지 않은 경우
    else:
        print(0)