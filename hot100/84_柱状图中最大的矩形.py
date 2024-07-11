class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n,he,ta=len(heights),0,0
        stk=[0]*n
        l,r=[-1]*n,[n]*n
        for i in range(n):
            while he<ta and heights[stk[ta-1]]>heights[i]:
                ta-=1
                r[stk[ta]]=i
            stk[ta]=i
            ta+=1
        he=ta=0
        for i in range(n-1,-1,-1):
            while he<ta and heights[stk[ta-1]]>heights[i]:
                ta-=1
                l[stk[ta]]=i
            stk[ta]=i
            ta+=1
        ans=0
        maxn=0
        for i in range(n):
            maxn=max(maxn,(r[i]-l[i]-1)*heights[i])
        return maxn





if __name__ == '__main__':
    solution = Solution()
    heights = [2,1,5,6,2,3]
    print(solution.largestRectangleArea(heights))





