text = input()

is_bracket = False
res = ""
buffer = ""
for c in text:
    if c == "<":
        is_bracket = True

        if buffer:
            res += " ".join([b[::-1] for b in buffer.split(" ")])
            buffer = ""

    elif c == ">":
        is_bracket = False
        res += c
        continue

    if is_bracket:
        res += c
    else:
        buffer += c

if buffer:
    res += " ".join([b[::-1] for b in buffer.split(" ")])

print(res)