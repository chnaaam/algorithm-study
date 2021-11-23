N = int(input())
commands = [input() for _ in range(N)]

result = ""
for i in range(len(commands[0])):
    is_correct = True
    current_c = commands[0][i]

    for command in commands:
        if not(command[i] == current_c):
            is_correct = False
            break

    if is_correct:
        result += current_c
    else:
        result += "?"

print(result)