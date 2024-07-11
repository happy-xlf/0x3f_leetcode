#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   54_螺旋矩阵.py
@Time    :   2024/05/18 10:14:48
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(matrix), len(matrix[0])
        lun = int(n/2+0.5)
        bn, bm = 0, 0
        en, em = n, m
        res = []
        flag = [(0,1),(1,0),(0,-1),(-1,0)]
        res.append(matrix[0][0])
        newx =0
        newy = 0
        while lun!=0:
            for idx,it in enumerate(flag):
                newx = newx+it[0]
                newy = newy+it[1]
                f=0
                while newx<en and newy<em and newx>=bn and newy>=bm:
                    if idx==3 and newx==bn and newy==bm:
                        break
                    res.append(matrix[newx][newy])
                    f=1
                    newx = newx+it[0]
                    newy = newy+it[1]
                newx = newx - it[0]
                newy = newy - it[1]
                if f==0 and (idx>=1):
                    break
            bn+=1
            bm+=1
            en-=1
            em-=1
            lun-=1
        print(res)

    def simple(self, matrix):
        if not matrix: return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        res = []

        while True:
            # 从左到右
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b: break

            # 从上到下
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r: break

            # 从右到左
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b: break

            # 从下到上
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res
        
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s = Solution()
    s.spiralOrder(matrix)


