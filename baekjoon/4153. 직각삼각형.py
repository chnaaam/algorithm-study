while True:
    num_list = [int(n) for n in input().split(" ")]
    if sum(num_list) == 0:
        break
        
    num_list.sort()

    A, B, C = num_list

    if A ** 2 + B ** 2 == C ** 2:
        print("right")
    else:
        print("wrong")

