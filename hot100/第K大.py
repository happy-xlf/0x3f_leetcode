class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums,l,r):
            value=nums[l]
            # bg=l
            while l<r:
                while l<r and nums[r]<=value:
                    r-=1
                nums[l]=nums[r]
                while l<r and nums[l]>=value:
                    l+=1
                nums[r]=nums[l]
                # if l<r:
                #     nums[l],nums[r]=nums[r],nums[l]
            # nums[bg],nums[l]=nums[l],nums[bg]
            nums[l]=value
            print(nums)
            return l

        n=len(nums)
        l=0
        r=n-1
        while True:
            idx=partition(nums,l,r)
            print("idx:",idx)
            if idx==k-1:
                return nums[k-1]
            elif idx<k-1:
                l=idx+1
            else:
                r=idx-1

if __name__ == '__main__':
    solution = Solution()
    arr = [3,2,1,5,6,4]
    k = 2
    print(solution.findKthLargest(arr,k))

