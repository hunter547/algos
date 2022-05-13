from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inorder(root):
            nonlocal prev
            if root == None:
                return True
            if not inorder(root.left):
                return False
            if prev != None and root.val <= prev:
                return False
            prev = root.val
            return inorder(root.right)
        return inorder(root)
