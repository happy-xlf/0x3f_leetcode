# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
#给定一个二叉搜索树的根节点 root ，和一个整数 k ，
#请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

# 解法1:
# 中序遍历则是他们的升序排列，要找第k小元素就是中序遍历的第k个元素
# k进行递减，直到k==0，则返回当前节点值
# 递归实现

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.k==0:
                return
            self.k-=1
            if self.k == 0:
                self.res = root.val
                return
            dfs(root.right)
        self.k = k
        dfs(root)
        return self.res