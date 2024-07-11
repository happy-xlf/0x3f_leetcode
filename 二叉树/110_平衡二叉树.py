#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   110_平衡二叉树.py
@Time    :   2024/04/01 17:24:46
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

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution2(object):

    def isBlanced(self, root):
        def get_depth(node):
            if not node:
                return 0
            left = get_depth(node.left)
            if left == -1:
                return -1
            right = get_depth(node.right)
            if right == -1 or abs(right-left)>1:
                return -1
            return max(left, right)+1
        return get_depth(root) != -1