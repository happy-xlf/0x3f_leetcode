class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix:
            return 0
        m,n=len(matrix),len(matrix[0])
        
        pre=[0]*(n+1)
        res=0
        for i in range(m):
            for j in range(n):
                pre[j]=pre[j]+1 if matrix[i][j]=='1' else 0
        
            stack=[-1]
            for k,num in enumerate(pre):
                while stack and num<pre[stack[-1]]:
                    index=stack.pop()
                    res=max(res,pre[index]*(k-stack[-1]-1))
                stack.append(k)
        return res
        
        
        
        


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
        ]
    print(solution.maximalRectangle(matrix))


