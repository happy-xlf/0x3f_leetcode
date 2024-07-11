#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   101_对称二叉树.py
@Time    :   2024/04/01 17:21:33
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSame(self, p, q):
        if p == None or q == None:
            return p is q
        return p.val == q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isSame(root.left, root.right)
        