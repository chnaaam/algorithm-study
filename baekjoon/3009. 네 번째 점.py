ax, ay = [int(n) for n in input().split(" ")]
bx, by = [int(n) for n in input().split(" ")]
cx, cy = [int(n) for n in input().split(" ")]

points = [(ax, ay), (bx, by), (cx, cy)]
p_dict = {}

for x, y in points:
    if f"{x}x" not in p_dict:
        p_dict[f"{x}x"] = []

    if f"{y}y" not in p_dict:
        p_dict[f"{y}y"] = []

    p_dict[f"{x}x"].append(x)
    p_dict[f"{y}y"].append(y)

x, y = -1, -1
for key, values in p_dict.items():
    if len(values) == 1:
        if "x" in key:
            x = values[0]
        else:
            y = values[0]

print(x, y)