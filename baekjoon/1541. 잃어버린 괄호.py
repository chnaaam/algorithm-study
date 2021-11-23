def parse(expr):
    terms = []
    for e1 in expr.split("-"):
        for e2 in e1.split("+"):
            terms.append(e2)
            terms.append("+")

        del terms[-1]
        terms.append("-")
    del terms[-1]

    return terms


expr = input()
minus_memory = []
is_minus_op = False
answer = 0

terms = parse(expr)

for term in terms:
    if term == "-":
        if minus_memory:
            answer -= sum(minus_memory)
            minus_memory = []

        is_minus_op = True
    elif term == "+":
        continue
    else:
        term = int(term)
        if not is_minus_op:
            answer += term
        else:
            minus_memory.append(term)

print(answer - sum(minus_memory))