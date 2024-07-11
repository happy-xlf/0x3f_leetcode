#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   100_相同的树.py
@Time    :   2024/04/01 17:19:34
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)