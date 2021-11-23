buffer = []

for i in range(10000):
    buffer.append(i + sum([int(c) for c in str(i)]))

buffer.sort()

for i in range(10000):
    if i not in buffer:
        print(i)