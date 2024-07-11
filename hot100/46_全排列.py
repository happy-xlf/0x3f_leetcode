class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        
        dfs(nums,[])
        return res




if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print(solution.permute(nums))


