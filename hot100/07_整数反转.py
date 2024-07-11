class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=-1
            x=abs(x)
        x=int(str(x)[::-1])
        x=x*flag   
        if x<-2**31 or x>2**31-1:
            return 0
        return x



if __name__ == '__main__':
    solution = Solution()
    x=120
    print(solution.reverse(x))
