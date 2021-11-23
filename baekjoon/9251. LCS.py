"""
점화식
if string1[i] == string2[j]:
    M[i][j]= M[i - 1][j - 1] + 1
else:
    M[i][j] = max(M[i - 1][j], M[i][j - 1])
"""

string1 = input()
string2 = input()

len_string1 = len(string1)
len_string2 = len(string2)

M = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]

max_value = 0
for i in range(len_string1):
    for j in range(len_string2):
        if string1[i] == string2[j]:
            M[i][j] = M[i - 1][j - 1] + 1

            if max_value < M[i][j]:
                max_value = M[i][j]
        else:
            M[i][j] = max(M[i - 1][j], M[i][j - 1])

print(max_value)