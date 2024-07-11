class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # l,r
        # [l,r], [l+1,r], ... [r,r]
        # r-l+1
        res = 0
        l = 0
        s = 1
        for r,x in enumerate(nums):
            s *= x
            while s  >= k and l<=r:
                s /= nums[l]
                l += 1
            if s < k:
                res+=r-l+1
        return res


if __name__ == '__main__':
    nums = [int(n) for n in input("nums:").split(",")]
    k = int(input("k:"))
    s= Solution()
    print(s.numSubarrayProductLessThanK(nums,k))