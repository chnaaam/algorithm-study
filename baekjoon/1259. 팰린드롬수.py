while True:
    text = input()

    if text == "0":
        break

    len_text = len(text) // 2
    is_palindrome = True

    for i in range(len_text):
        if text[i] != text[(-1) * (i + 1)]:
            is_palindrome = False
            break

    if is_palindrome:
        print("yes")
    else:
        print("no")


