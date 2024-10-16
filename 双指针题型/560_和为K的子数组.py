from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        res = 0
        dt = {}
        dt[0] = 1
        for it in nums:
            pre += it
            if pre - k in dt:
                res+=dt[pre-k]
            dt[pre] = dt.get(pre, 0) + 1
        return res
                
if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, 0]
    k = 0
    print(s.subarraySum(nums,k))