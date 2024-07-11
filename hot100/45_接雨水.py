class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        maxleft=[0]*n
        maxright=[0]*n
        maxleft[0]=height[0]
        maxright[n-1]=height[n-1]

        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i])
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i])
        res=0
        for i in range(n):
            res+=min(maxleft[i],maxright[i])-height[i]
        return res
    
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n=len(height)
        left=0
        right=n-1
        res=0
        maxleft=height[0]
        maxright=height[n-1]
        while left<=right:
            maxleft=max(maxleft,height[left])
            maxright=max(maxright,height[right])

            if maxleft<maxright:
                res+=maxleft-height[left]
                left+=1
            else:
                res+=maxright-height[right]
                right-=1

        return res




if __name__ == '__main__':
    solution = Solution()
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    print(solution.trap2(height))
