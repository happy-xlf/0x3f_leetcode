#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   48_旋转图像.py
@Time    :   2024/10/16 11:36:22
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().rotate(matrix))