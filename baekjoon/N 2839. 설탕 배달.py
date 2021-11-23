while True:
    N = int(input())
    answer = 0

    while True:
        if N >= 5 and N % 3 != 0:
            N -= 5
            answer += 1
            continue

        elif N >= 3:
            N -= 3
            answer += 1

        if N == 0:
            print(answer)
            break

        elif N <= 2:
            print(-1)
            break