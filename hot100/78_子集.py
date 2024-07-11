class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        def dfs(index,nums,tmp):
            if index==len(nums):
                return
            for i in range(index,len(nums)):
                tmp.append(nums[i])
                res.append(tmp[:])
                dfs(i+1,nums,tmp)
                tmp.pop()
        dfs(0,nums,[])
        return res



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print(solution.subsets(nums))
