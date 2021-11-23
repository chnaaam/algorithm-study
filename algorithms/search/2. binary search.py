"""
Binary Search
배열을 절반으로 쪼개가면서

조건 : 정렬된 배열이여야 함함
Time Complexity : O(n)

Binary Search나 Hashtable에 비해 속도가 늦기 때문에 거의 사용하지 않음
"""


def solution(arr, N, K):
    left, right = 0, N - 1

    while left <= right:

        # Case 1
        # 아래의 경우 left와 right의 합이 integer 표현 범위보다 큰 경우
        # 값이 제대로 계산되지 않을수도 있기 때문에 사용할 수 없음음

       # middle = (left + right) // 2

        # Case 2
        middle = left + (right - left) // 2

        if arr[middle] == K:
            return middle

        elif arr[middle] < K:
            left = middle + 1

        else:
            right = middle - 1

    return -1

# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# N = 10
# K = 38

arr = [1, 2, 3, 4, 6]
N = 5
K = 6

assert solution(arr, N, K) == 4