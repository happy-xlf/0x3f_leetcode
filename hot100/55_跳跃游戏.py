class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i
        return target==0
    
    def canJump2(self, nums):
        ans={}
        def dfs(nums,index):
            if index>=len(nums)-1:
                return True
            if index in ans:
                return ans[index]
            for i in range(1,nums[index]+1):
                if dfs(nums,index+i):
                    ans[index]=True
                    return True
            ans[index]=False
            return False
        dfs(nums,0)
        






if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))



