#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   73_矩阵置零.py
@Time    :   2024/10/16 10:41:56
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix