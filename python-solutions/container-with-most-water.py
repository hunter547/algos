from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = 0
        left = 0
        right = len(height) - 1
        while left < right:
            current_max = min(height[left], height[right]) * (right - left)
            max_height = max(max_height, current_max)
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return max_height
