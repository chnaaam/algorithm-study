nums = [1,1,1,1,1]
target = 3

def findTargetSumWays(nums, target) -> int:
        
    len_nums = len(nums)
    
    cnt = 0

    def dfs(current_sum, i):
        
        if len_nums == i:
            if current_sum == target:
                global cnt
                cnt = cnt + 1
            return

        dfs(current_sum + nums[i], i + 1)
        dfs(current_sum - nums[i], i + 1)

    dfs(0, 0)
    print(cnt)
    
findTargetSumWays(nums, target)