from typing import List
from collections import deque, defaultdict
# O(n) time complexity and O(n) space complexity
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        dict_level = defaultdict(deque)
        dq = deque([root])
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                if (level % 2 == 1):
                    dict_level[level].appendleft(node.val)
                else:
                    dict_level[level].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
        return dict_level.values()
