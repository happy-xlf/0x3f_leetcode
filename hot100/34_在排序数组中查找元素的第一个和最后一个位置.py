class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left=0
        right=len(nums)-1
        ans=[]
        while left<right:
            mid=(right-left)//2+left
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
        if nums[left]==target:
            ans.append(left)
            print(left)
            right=len(nums)-1
            while left<right:
                mid=(right-left)//2+left+1
                if nums[mid]<=target:
                    left=mid
                else:
                    right=mid-1
            ans.append(left)
        else:
            return [-1,-1]
        
        return ans

if __name__ == '__main__':
    solution = Solution()

    nums = [5,7,7,8,8,10]
    target = 8
    
    print(solution.searchRange(nums, target))


