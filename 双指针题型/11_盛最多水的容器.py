class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxn = 0
        while l < r:
            maxn=max(maxn,(r-l)*min(height[r],height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxn
    
    def maxArea2(self, height):
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            cur=min(height[left],height[right])*(right-left)
            # print(cur)
            max_area=max(max_area,cur)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_area


if __name__ == '__main__':
    nums = [int(n) for n in input().split(',')]
    s = Solution()
    print(s.maxArea(nums))
