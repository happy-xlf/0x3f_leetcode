#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix char字符型二维数组 
# @return int整型
#
from typing import List
# 最大面积
class Solution:
    def maximalSquare(self , matrix: List[List[str]]) -> int:
        # write code here
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        max_side = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side**2
print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))