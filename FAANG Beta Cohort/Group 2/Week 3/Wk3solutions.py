from collections import deque
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Validate Binary Search Tree - DFS
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        
        return True


    # Number of Island - BFS 
    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def bfs(self, grid, r, c):
        queue = deque([(r,c)])

        while queue:
            cr, cc = queue.popleft()
            for dr, dc in self.dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid, r, c)
        return count