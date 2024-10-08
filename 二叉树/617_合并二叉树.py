#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :617_合并二叉树.py
# @Time      :2024/08/06 11:11:00
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

def levelOrder(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res

if __name__ == "__main__":
    s = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)
    s.mergeTrees(root1, root2)
    # 分层遍历
    print(levelOrder(root1))