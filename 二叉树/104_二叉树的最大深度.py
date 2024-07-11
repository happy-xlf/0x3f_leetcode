#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   104_二叉树的最大深度.py
@Time    :   2024/03/27 18:04:15
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        l_sum = self.maxDepth(root.left)
        r_sum = self.maxDepth(root.right)
        return max(l_sum,r_sum)+1

