def isPalindrome(s):
    _s = ""
    for c in s:
        if c.isalnum():
            _s += c

    s = _s
    s = s.lower()

    len_s = len(s)
    middle_idx = int(len_s / 2 + 0.5)

    for i in range(middle_idx):
        if s[i] != s[len_s - i - 1]:
            return False

    return True

# print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))