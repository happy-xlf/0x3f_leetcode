class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right) //2
            if nums[mid]==target:
                return mid
            #证明左侧是有序数组
            if nums[mid]>nums[left]:
                if nums[left]<= target <=nums[mid]:
                    right=mid
                else:
                    left=mid+1
            else:
                #右侧为有序数组
                if nums[mid+1]<= target <=nums[right]:
                    left=mid+1
                else:
                    right=mid
        return left if nums[left]==target else -1

if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(solution.search(nums, target))

