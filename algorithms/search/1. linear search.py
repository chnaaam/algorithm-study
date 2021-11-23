"""
Linear Search
N개의 숫자를 포함한 배열 arr와 숫자 K가 주어졌을 때, arr 내 가장 첫 번째 K의 위치를 찾는 방법
만약 K를 포함하지 않는다면 -1을 리턴함

Time Complexity : O(n)

Binary Search나 Hashtable에 비해 속도가 늦기 때문에 거의 사용하지 않음
"""

def solution(arr, K):
    for i in range(len(arr)):
        if arr[i] == K:
            return i

    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
K = 110

assert solution(arr, K) == 6