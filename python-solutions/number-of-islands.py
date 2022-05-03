from typing import List

# Depth First Search approach


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == "1"):
                    islands += self.dfs(grid, r, c)

        return islands

    def dfs(self, grid: List[List[str]], row: int, col: int) -> int:
        # We're checking out of bounds above, below, left or right of the grid, or current position is water, then return
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return 0

        # Set the island as seen (i.e. set to water so that future iterations don't confuse this as an unforseen island)
        grid[row][col] = '0'

        # Check the cell above for land
        self.dfs(grid, row + 1, col)
        # Check the cell below for land
        self.dfs(grid, row - 1, col)
        # Check the cell to the right for land
        self.dfs(grid, row, col + 1)
        # Check the cell to the left for land
        self.dfs(grid, row, col - 1)

        # return 1 for an island found after all recursive work is done and all found land surrounding this land piece is set to water
        return 1
