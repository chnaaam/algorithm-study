import re

def isPalindrome(s):
    val = re.sub('[^A-Za-z0-9]', '', s).lower()
    middle_idx = int(len(val) / 2 + 0.5)
    if val[:middle_idx] == val[::-1][:middle_idx]:
        return True
    return False

# print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))