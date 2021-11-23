N = int(input())
cute = 0

for _ in range(N):
    X = int(input())

    if X == 1:
        cute += 1
    else:
        cute -= 1

if cute > 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
