"""
LeetCode 1260 - Shift 2D Grid

Pattern:
- Matrix
- Index Mapping

Approach:
- Treat the 2D grid as a 1D array.
- Convert each cell's (row, col) to a 1D index.
- Shift the index by k using modulo to wrap around.
- Convert the shifted index back to (row, col).
- Place the element in its new position.

Time Complexity:
O(rows × cols)

Space Complexity:
O(rows × cols)
"""
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        rows = len(grid)
        cols = len(grid[0])

        k %= (rows * cols)

        answer = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                current_index = i * cols + j
                new_index = (current_index + k) % (rows * cols)

                new_row = new_index // cols
                new_col = new_index % cols

                answer[new_row][new_col] = grid[i][j]

        return answer
