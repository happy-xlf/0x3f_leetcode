#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :222_完全二叉树的节点个数.py
# @Time      :2024/07/24 09:55:05
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(s.countNodes(root))







