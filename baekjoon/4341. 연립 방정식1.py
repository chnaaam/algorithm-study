

# N = int(input())
# for _ in range(N):
# expr_A = "2x + 3y = x"#input()
# expr_B = "5 = x + y + 3"#input()

# expr_A = "2x + 3y = 0"
# expr_B = "10x = -15y"

# expr_A = "2x + 3y = 0"
# expr_B = "10x = -15y + 1"
# #
# expr_A = "x = 1"
# expr_B = "3x = 6y"
# #
# expr_A = "2x = 3x + -x + y"
# expr_B = "x + y = x + y"
#
# expr_A = "2x = -3"
# expr_B = "-2y = 3"
#
# expr_A = "1 = 2"
# expr_B = "x = 3"

# expr_A = "1 = 2"
# expr_B = "x = 3"

from collections import deque
from math import gcd

def get_expr_dict(expr):
    if not expr:
        return {"x": 0, "y": 0, "n": 0}

    expr_q = deque(expr.split(" "))
    term_dict = {"x": 0, "y": 0, "n": 0}

    is_plus = 1
    is_right_term = 1

    while expr_q:
        term = expr_q.popleft()

        if term == "-":
            is_plus = -1
            continue
        elif term == "+":
            is_plus = 1
            continue
        elif term == "=":
            is_right_term = -1
            continue

        if term.endswith("x"):
            if term == "x":
                term_dict["x"] += is_plus * is_right_term * 1
            elif term == "-x":
                term_dict["x"] += is_plus * is_right_term * -1
            else:
                if not term.startswith("-"):
                    term_dict["x"] += is_plus * is_right_term * int(term[:-1])
                else:
                    term_dict["x"] += (-1) * is_plus * is_right_term * int(term[1:-1])

        elif term.endswith("y"):
            if term == "y":
                term_dict["y"] += is_plus * is_right_term * 1
            elif term == "-y":
                term_dict["y"] += is_plus * is_right_term * -1
            else:
                if not term.startswith("-"):
                    term_dict["y"] += is_plus * is_right_term * int(term[:-1])
                else:
                    term_dict["y"] += (-1) * is_plus * is_right_term * int(term[1:-1])

        else:
            term_dict["n"] += is_plus * is_right_term * int(term)

        is_plus = 1

    term_dict["n"] *= -1

    return term_dict


def get_fraction(x, d):
    gcd_x = gcd(x, d)

    if x == 0:
        return 0
    elif (x > 0 and d > 0) or (x < 0 and d < 0):
        plus = 1
    else:
        plus = -1

    x, d = abs(x), abs(d)

    if d == 0:
        result = 0
    else:
        if plus == -1:
            result = "-"
        else:
            result = ""

        if x == 1:
            if d == 1:
                result += str(1)
            else:
                result += f"1/{d}"
        else:
            if d == gcd_x:
                result += f"{x // gcd_x}"
            elif x == gcd_x:
                result += f"1/{d // gcd_x}"
            else:
                result += f"{x // gcd_x}/{d // gcd_x}"

    return result

# N = int(input())
N = 7
for i, (expr_A, expr_B) in enumerate([
    # ("2x + 3y = x", "5 = x + y + 3"),
    # ("2x + 3y = 0", "10x = -15y"),
    # ("2x + 3y = 0", "10x = -15y + 1"),
    # ("x = 1", "3x = 6y"),
    # ("2x = 3x + -x + y", "x + y = x + y"),
    # ("2x = -3", "-2y = 3"),
    # ("1 = 2", "x = 3"),
    # ("", "y = 3"),
    # ("x = 1", "x = 3"),
    # ("y = -1", "-2x = 3"),
    # ("", ""),
    # ("2x - 5 + y = 9", "1 + -y = 3"),
    # ("3 = 2x", "3y = 2"),
    # ("x + 2y = -1", "2x + 1y = -1"),
    # ("-3x - 3 = 10", "10 = -3x - 3"),
    # ("2x = 1", "2 = 4x"),
    # ("x = 0", "0 = 2y")
    ("2 + 2y = 1", "2x + 3y = 1")
]):
# for i in range(N):
#     # expr_A = input()
#     # expr_B = input()
#
#     expr_A = "2x + 3y = 0"
#     expr_B = "10x = -15y"

    # expr_A = "2x + 3y = 0"
    # expr_B = "10x = -15y + 1"
    # #
    # expr_A = "x = 1"
    # expr_B = "3x = 6y"

    # expr_A = "2x = 3x + -x + y - 2 + 4 - 10"
    # expr_B = "x + y = x + y"

    # expr_A = "2x = -3"
    # expr_B = "-y = 3"

    # expr_A = ""
    # expr_B = "x = 3"

    print(expr_A)
    print(expr_B)

    term_dict_A = get_expr_dict(expr_A)
    term_dict_B = get_expr_dict(expr_B)

    gauss = term_dict_A["x"] * term_dict_B["y"] - term_dict_A["y"] * term_dict_B["x"]

    if gauss == 0:
        if term_dict_A["x"] == 0 and term_dict_A["y"] == 0 and term_dict_A["n"] == 0:
            if term_dict_B["x"] == 0 and term_dict_B["y"] == 0 and term_dict_B["n"] == 0:
                print("don't know")
                print("don't know")
            elif term_dict_B["x"] == 0:
                print("don't know")
                print(get_fraction(term_dict_B["n"], term_dict_B["y"]))
            elif term_dict_B["y"] == 0:
                print(get_fraction(term_dict_B["n"], term_dict_B["x"]))
                print("don't know")
            else:
                print("don't know")

        elif term_dict_B["x"] == 0 and term_dict_B["y"] == 0 and term_dict_B["n"] == 0:
            if term_dict_A["x"] == 0 and term_dict_A["y"] == 0 and term_dict_A["n"] == 0:
                print("don't know")
                print("don't know")
            elif term_dict_A["x"] == 0:
                print("don't know")
                print(get_fraction(term_dict_A["n"], term_dict_A["y"]))
            elif term_dict_A["y"] == 0:
                print(get_fraction(term_dict_A["n"], term_dict_A["x"]))
                print("don't know")
            else:
                print("don't know")

        else:
            if term_dict_A["x"] != 0 and term_dict_B["x"] != 0:
                if term_dict_A["n"] / term_dict_A["x"] == term_dict_B["n"] / term_dict_B["x"]:
                    print(get_fraction(term_dict_A["n"], term_dict_A["x"]))
                else:
                    print("don't know")
                print("don't know")

            elif term_dict_A["y"] != 0 and term_dict_B["y"] != 0:
                print("don't know")
                if term_dict_A["n"] / term_dict_A["y"] == term_dict_B["n"] / term_dict_B["y"]:
                    print(get_fraction(term_dict_A["n"], term_dict_A["y"]))
                else:
                    print("don't know")

            else:
                print("don't know")
                print("don't know")

    else:
        term_dict_A["x"], term_dict_B["y"] = term_dict_B["y"], term_dict_A["x"]

        term_dict_A["y"] *= -1
        term_dict_B["x"] *= -1

        x = term_dict_A["x"] * term_dict_A["n"] + term_dict_A["y"] * term_dict_B["n"]
        y = term_dict_B["x"] * term_dict_A["n"] + term_dict_B["y"] * term_dict_B["n"]

        print(get_fraction(x, gauss))
        print(get_fraction(y, gauss))

    # if i < N - 1:
    print()
