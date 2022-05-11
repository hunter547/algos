from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0

        def dfs(root):
            nonlocal sum
            if (root == None):
                return
            if (low <= root.val and root.val <= high):
                sum += root.val
            if low < root.val:
                dfs(root.left)
            if high > root.val:
                dfs(root.right)
        dfs(root)
        return sum
