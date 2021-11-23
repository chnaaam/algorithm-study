N = int(input())
triangle = []
for _ in range(N):
    triangle.append([int(n) for n in input().split(" ")])

if N == 1:
    print(triangle[0][0])
elif N == 2:
    print(max(triangle[1]) + triangle[0][0])
else:
    m = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]

    for depth in range(2, N):
        new_m = [0] * (depth + 1)
        new_m[0] = m[0] + triangle[depth][0]
        new_m[depth] = m[depth - 1] + triangle[depth][depth]

        for i in range(1, len(triangle[depth]) - 1):
            # 최대가 되는 경로를 구하는 것이 목표이기 때문에
            # 이전 두 개의 노드로부터 생성되는 값 2개를 모두 계산, 저장하지 않고
            # 값이 큰 하나만 저장하면 된다.
            new_m[i] = max(m[i - 1], m[i]) + triangle[depth][i]

        m = new_m

    print(max(m))