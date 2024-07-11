class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def solve(k):
            n=0
            for it in nums:
                if n<k or nums[n-k]!=it:
                    nums[n]=it
                    n+=1
            return n
        return solve(2)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,1,2,2,2,2,3]
    print(solution.removeDuplicates(nums))
