class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                k=nums.index(target-nums[i])
                if k!=i:
                    return [i,k]    

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    s=Solution()
    ans=s.twoSum(nums,target)
    print(ans)