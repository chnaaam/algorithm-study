N = int(input())#5
arr = [int(n) for n in input().split(" ")]#[-2, 4, -99, -1, 98]

# N = 5
# arr = [1, 2, 3]#-2, 4, -1, 98]

arr.sort()
min_value = 2000000000

left, right = 0, len(arr) - 1
idx1, idx2 = left, right

while left < right:
    tmp = arr[left] + arr[right]
    
    if abs(tmp) == 0:
        idx1, idx2 = left, right
        break
    
    elif abs(tmp) < min_value:
        min_value = abs(tmp)
        idx1, idx2 = left, right
    
    if 0 < tmp:
        right -= 1
    else:
        left += 1
        
print(arr[idx1], arr[idx2])

