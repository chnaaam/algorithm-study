from collections import deque
from math import gcd


def parse_expression(expr):
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


expr_A, expr_B = ("2 + 2y = 1", "2x + 3y = 1")

termA = parse_expression(expr_A)
termB = parse_expression(expr_B)

denominator = termA["x"] * termB["y"] - termA["y"] * termB["x"]

# 역행렬이 안되는 경우
if denominator != 0:
    termA["x"], termB["y"] = termB["y"], termA["x"]

    termA["y"] *= -1
    termB["x"] *= -1

    print(get_fraction(termA["x"] * termA["n"] + termA["y"] * termB["n"], denominator))
    print(get_fraction(termB["x"] * termA["n"] + termB["y"] * termB["n"], denominator))
else:
    if termA["n"] == 0:
        pass
    elif termB["n"] == 0:
        pass


    if termA["x"] == 0 and termA["y"] == 0 and termA["n"] == 0:
        pass

    elif termB["x"] == 0 and termB["y"] == 0 and termB["n"] == 0:
        pass



# if gauss == 0:
#     if term_dict_A["x"] == 0 and term_dict_A["y"] == 0 and term_dict_A["n"] == 0:
#         if term_dict_B["x"] == 0 and term_dict_B["y"] == 0 and term_dict_B["n"] == 0:
#             print("don't know")
#             print("don't know")
#         elif term_dict_B["x"] == 0:
#             print("don't know")
#             print(get_fraction(term_dict_B["n"], term_dict_B["y"]))
#         elif term_dict_B["y"] == 0:
#             print(get_fraction(term_dict_B["n"], term_dict_B["x"]))
#             print("don't know")
#         else:
#             print("don't know")
#
#     elif term_dict_B["x"] == 0 and term_dict_B["y"] == 0 and term_dict_B["n"] == 0:
#         if term_dict_A["x"] == 0 and term_dict_A["y"] == 0 and term_dict_A["n"] == 0:
#             print("don't know")
#             print("don't know")
#         elif term_dict_A["x"] == 0:
#             print("don't know")
#             print(get_fraction(term_dict_A["n"], term_dict_A["y"]))
#         elif term_dict_A["y"] == 0:
#             print(get_fraction(term_dict_A["n"], term_dict_A["x"]))
#             print("don't know")
#         else:
#             print("don't know")
#
#     else:
#         if term_dict_A["x"] != 0 and term_dict_B["x"] != 0:
#             if term_dict_A["n"] / term_dict_A["x"] == term_dict_B["n"] / term_dict_B["x"]:
#                 print(get_fraction(term_dict_A["n"], term_dict_A["x"]))
#             else:
#                 print("don't know")
#             print("don't know")
#
#         elif term_dict_A["y"] != 0 and term_dict_B["y"] != 0:
#             print("don't know")
#             if term_dict_A["n"] / term_dict_A["y"] == term_dict_B["n"] / term_dict_B["y"]:
#                 print(get_fraction(term_dict_A["n"], term_dict_A["y"]))
#             else:
#                 print("don't know")
#
#         else:
#             print("don't know")
#             print("don't know")
#
# else:
#     term_dict_A["x"], term_dict_B["y"] = term_dict_B["y"], term_dict_A["x"]
#
#     term_dict_A["y"] *= -1
#     term_dict_B["x"] *= -1
#
#     x = term_dict_A["x"] * term_dict_A["n"] + term_dict_A["y"] * term_dict_B["n"]
#     y = term_dict_B["x"] * term_dict_A["n"] + term_dict_B["y"] * term_dict_B["n"]
#
#     print(get_fraction(x, gauss))
#     print(get_fraction(y, gauss))
