#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型二维数组
#
from typing import List
#找组合
class Solution:
    def combinationSum2(self , nums: List[int], target: int) -> List[List[int]]:
        # write code here
        def dfs(nums, target, start, path, res):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)
        nums.sort()
        res = []
        dfs(nums, target, 0, [], res)
        return res
s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))