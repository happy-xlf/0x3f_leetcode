from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return nums

if __name__ == '__main__':
    nums = [0,0,1]
    s = Solution()
    print(s.moveZeroes(nums))