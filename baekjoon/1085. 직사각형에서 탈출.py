x, y, w, h = [int(n) for n in input().split(" ")]

def calc_min(a, b):
    if (a - 0) > (b - a):
        min = b - a
    else:
        min = a

    return min

min_x = calc_min(x, w)
min_y = calc_min(y, h)

if min_y > min_x:
    print(min_x)
else:
    print(min_y)