N = int(input())
buildings = [int(input()) for _ in range(N)]

answers = [0] * N
stack = []

for current_b_idx, b in enumerate(buildings):
    while stack and buildings[stack[-1]] < b:
        previous_b_idx = stack.pop()
        answers[previous_b_idx] = current_b_idx - previous_b_idx - 1
    stack.append(current_b_idx)


if stack:
    for i in range(len(stack)):
        answers[stack[i]] = N - stack[i] - 1
    
print(sum(answers))