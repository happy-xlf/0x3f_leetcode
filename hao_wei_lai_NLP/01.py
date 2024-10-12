#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
from typing import List

#找出数组中成绩最大的非空连续子数组，并返回该子数组的乘积
# 最大非空连续子数组
class Solution:
    def maxProduct(self , nums: List[int]) -> int:
        # write code here
        if not nums:
            return 0
        max_product = nums[0]
        min_product = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            max_product,min_product = max(max_product*nums[i],min_product*nums[i],nums[i]),min(max_product*nums[i],min_product*nums[i],nums[i])
            res = max(res,max_product)
        return res
s = Solution()
print(s.maxProduct([2,3,-2,4]))