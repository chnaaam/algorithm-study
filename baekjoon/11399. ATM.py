N = int(input())
people = [int(n) for n in input().split(" ")]

people.sort()
sum = 0
interval = 0
for p in people:
    sum += interval + p
    interval += p

print(sum)