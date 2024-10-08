#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :107_二叉树的层序遍历 II.py
# @Time      :2024/08/06 11:17:02
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root:
            queue.append(root)
        res = []
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res[::-1]

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.levelOrderBottom(root))