class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+k==0:
                    ans.append([k,nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+k<0:
                    left+=1
                else:
                    right-=1
        return ans
                
        



if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))
