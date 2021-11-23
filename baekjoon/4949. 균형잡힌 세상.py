while True:
    bracket = []

    sentence = input()

    if sentence == ".":
        break

    is_correct = "yes"

    for c in sentence:
        if c == "(":
            bracket.append(c)
        elif c == "[":
            bracket.append(c)
        elif c == ")":
            if bracket:
                if bracket[-1] != "(":
                    is_correct = "no"
                    break

                bracket.pop()
            else:
                is_correct = "no"
                break
        elif c == "]":
            if bracket:
                if bracket[-1] != "[":
                    is_correct = "no"
                    break

                bracket.pop()
            else:
                is_correct = "no"
                break

    if bracket:
        is_correct = "no"

    print(is_correct)

