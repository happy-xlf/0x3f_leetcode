#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :153_二叉树中和为目标值的路径.py
# @Time      :2024/07/20 15:00:07
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/description/

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res, path = [], []
        def dfs(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        
        dfs(root, target)
        return res 



if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(s.pathTarget(root, 22))