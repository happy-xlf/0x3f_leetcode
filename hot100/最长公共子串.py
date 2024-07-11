class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        if len(str1) <len(str2):
            str1,str2 = str2,str1
        res=''
        maxlen=0
        for i in range(len(str1)):
            if str1[i-maxlen:i+1] in str2:
                res=str1[i-maxlen:i+1]
                maxlen+=1
        if len(res)==0:
            return -1
        return res
    
if __name__ == '__main__':
    str1="1AB2345CD"
    str2="12345EF"
    solution=Solution()
    print(solution.LCS(str1=str1,str2=str2))

