#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :105_从前序与中序遍历序列构造二叉树.py
# @Time      :2024/07/29 14:20:57
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

def dfs(root):
    if not root:
        return
    print(root.val)
    dfs(root.left)
    dfs(root.right)

def middfs(root):
    if not root:
        return
    middfs(root.left)
    print(root.val)
    middfs(root.right)

if __name__ == "__main__":
    s = Solution()
    root = s.buildTree([3,9,20,15,7],[9,3,15,20,7])
    # 层序遍历root
    # dfs(root)
    middfs(root)
