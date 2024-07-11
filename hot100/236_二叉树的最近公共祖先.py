# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 思维：从root节点开始左右子树分别向下搜索
        # 递归判断条件是：如果root为None，则返回None；如果当前root==p或q，则返回root；
        # 递归左右子树，分以下几种情况：
        # 1.左右子树均返回值，表明p和q分别在左右两个分支，则root为最近的祖先
        # 2.右子树返回None，表明p和q都在左分支，则左子树返回的是最近的祖先
        # 3.左子树返回None，表明p和q都在右分支，则右子树返回的是最近的祖先
        # 4.左右子树均返回None，表明p和q不在root的左右两个分支，则返回None
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left == None and right:
            return right
        if left and right == None:
            return left
        if left == None and right == None:
            return None
