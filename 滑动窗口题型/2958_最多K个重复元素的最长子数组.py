class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        dit = {}
        maxn = 0
        for r, x in enumerate(nums):
            dit[x] = dit.get(x,0) + 1
            while dit[x] > k:
                dit[nums[l]]-=1
                l+=1
            maxn =max(maxn, r-l+1)
        return maxn

if __name__ == '__main__':
    nums = [int(n) for n in input("nums:").split(",")]
    k = int(input("k:"))
    s = Solution()
    print(s.maxSubarrayLength(nums, k))
