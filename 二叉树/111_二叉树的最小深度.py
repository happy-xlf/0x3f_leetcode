#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   111_二叉树的最小深度.py
@Time    :   2024/03/27 18:07:20
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        l_sum = 1e9
        r_sum = 1e9
        if root.left != None:
            l_sum = self.minDepth(root.left)
        if root.right != None:
            r_sum = self.minDepth(root.right)
        if l_sum == r_sum and l_sum==1e9:
            return 1
        return min(l_sum,r_sum)+1
        