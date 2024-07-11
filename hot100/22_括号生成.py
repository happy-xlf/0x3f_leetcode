class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #()()()
        def dfs(n,left,right,path):
            if left>n or right>left: return 
            if len(path) == 2*n:
                ans.append(path)
            
            dfs(n,left+1,right,path+'(')
            dfs(n,left,right+1,path+')')

        ans=[]
        if n<=0:
            return ans
        dfs(n,0,0,'')

        return ans




if __name__ == '__main__':
    n=3
    solution=Solution()
    print(solution.generateParenthesis(n))


