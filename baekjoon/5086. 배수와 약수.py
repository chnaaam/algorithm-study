# 약수
def is_divisor(a, b):
    return b / a == b // a

# 배수
def is_multiple(a, b):
    return a / b == a // b

while True:
    a, b = [int(n) for n in input().split(" ")]

    if a == 0 and b == 0:
        break

    d = is_divisor(a, b)
    m = is_multiple(a, b)

    if not d and not m:
        print("neither")
    elif d:
        print("factor")
    else:
        print("multiple")