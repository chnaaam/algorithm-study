s = "123454321"

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    print(left, right)
    return s[left + 1 : right]

print(expand(3, 5))