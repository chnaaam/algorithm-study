N = int(input())
nums = [int(n) for n in input().split(" ")]#[5, 12, 7, 10, 9, 1, 2, 3, 11]
x = int(input())

nums.sort()
left, right = 0, len(nums) - 1
answer = 0

while left < right:
    data = nums[left] + nums[right]
    
    if data == x:
        answer += 1
        left += 1
    elif data < x:
        left += 1
    else:
        right -= 1
        
print(answer)