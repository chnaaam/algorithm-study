def isBadVersion(x):
    if x >= 2:
        return True
    else:
        return False

n = 2

def test():
    if isBadVersion(0):
        return 0
    elif isBadVersion(1):
        return 1
    else:
        for i in range(n, 1, -1):
            if isBadVersion(i) and not isBadVersion(i - 1):
                return i

print(test())