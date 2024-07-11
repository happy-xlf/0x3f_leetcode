class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))
