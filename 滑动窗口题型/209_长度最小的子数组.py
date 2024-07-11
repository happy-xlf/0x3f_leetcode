class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        min_length = len(nums)+1
        left = 0
        for right,x in enumerate(nums):
            s += nums[right]
            while s >= target:
                min_length = min(min_length, right - left + 1)
                s-=nums[left]
                left+=1
        return min_length if min_length <= len(nums) else 0


if __name__ == '__main__':
    target = int(input("target:"))
    nums = [int(n) for n in input("nums:").split(",")]
    s = Solution()
    print(s.minSubArrayLen(target,nums))