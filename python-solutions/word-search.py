from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # If dfs function has been called as many times as the length of the word,
            # we've found all letters in a row
            if i == len(word):
                return True
            # If the r or c is out of bounds of the graph, the character at our current index in the work
            # doesn't equal the current character being iterated over in the board, or we've already visited
            # this position in the board, then return false
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False

            # A match was found for the next character in the word for the given row and column in the board
            path.add((r, c))

            # Check all four surrounding cells if there is a match for the next character
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if (dfs(r, c, 0)):
                    return True

        return False
