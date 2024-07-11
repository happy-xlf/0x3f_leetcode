#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   166_珠宝的最高价值.py
@Time    :   2024/04/05 13:31:17
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def jewelleryValue(self, frame):
        """
        :type frame: List[List[int]]
        :rtype: int
        """
        n = len(frame)
        m = len(frame[0])

        dp=[[0]*m for _ in range(n)]
        dp[0][0]=frame[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+frame[i][0]
        for j in range(1,m):
            dp[0][j]=dp[0][j-1]+frame[0][j]

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] =max(dp[i-1][j],dp[i][j-1])+frame[i][j]

        return dp[-1][-1]



if __name__ == '__main__':
    frame = [[1,3,1],[1,5,1],[4,2,1]]
    s = Solution()
    print(s.jewelleryValue(frame))

