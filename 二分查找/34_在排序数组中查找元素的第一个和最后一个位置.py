class Solution(object):

    def lower_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1 # [mid+1, r]
            else:
                r = mid - 1 # [l, mid-1]
        return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.lower_search(nums, target)
        if nums[start] != target:
            return [-1, -1]
        else:
            end = self.lower_search(nums, target+1) - 1
            return [start, end]



if __name__ == '__main__':
    nums = [int(n) for n in input("nums:").split(",")]
    target = int(input("target:"))
    s = Solution()
    print(s.searchRange(nums, target))